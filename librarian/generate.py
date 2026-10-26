"""Answer a question from the retrieved chunks, with a citation for each claim.

    from librarian.generate import Librarian
    lib = Librarian()
    result = lib.ask("Combien faut-il sur le compte bloqué pour l'Allemagne ?")
    print(result.answer, result.citations)

Pipeline: hybrid search + reranker -> top K chunks -> the model answers only from
those chunks, citing them as [S1], [S2]..., and says it doesn't know when the
sources don't contain the answer. It returns JSON, so citations and "I don't
know" can be checked automatically. Every call records tokens, cost and latency
for the cost model.
"""

import json
import os
import re
import time
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from librarian.retrieve import Retriever

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

# Week 8: nano with high reasoning costs 69% less than mini (low) for -1.9 accuracy points
# (see optimisation.md). LIBRARIAN_MODEL=gpt-5.4-mini LIBRARIAN_EFFORT=low
# LIBRARIAN_NEWEST_FIRST=0 restores the Week 7 setup.
MODEL = os.getenv("LIBRARIAN_MODEL", "gpt-5.4-nano")
EFFORT = os.getenv("LIBRARIAN_EFFORT", "high")  # reasoning effort of the answer model
NEWEST_FIRST = os.getenv("LIBRARIAN_NEWEST_FIRST", "1") == "1"  # see newest_first()
USE_EXAMPLES = os.getenv("LIBRARIAN_EXAMPLES", "0") == "1"  # worked examples in the prompt (see EXAMPLES)
TOP_K = 4  # ~500 words of context with 150-word chunks (see eval/results/chunking-dev.md)

# USD per 1M tokens (input, cached input, output), from OpenAI's model pages, Oct 2026.
PRICES = {
    "gpt-5.4-mini": (0.75, 0.075, 4.50),
    "gpt-5.4-nano": (0.20, 0.02, 1.25),
}

# Fixed instructions first, so the provider can cache this prefix across requests.
INSTRUCTIONS = """You are the Librarian, an assistant for Tunisian students who want to study abroad \
(France, Germany, Canada, Erasmus+). You answer ONLY from the numbered sources provided with each \
question. You have no other knowledge.

Rules:
1. Use only facts stated in the sources. Never add facts from memory, even if you believe them true.
2. Put a citation like [S1] or [S2][S3] right after every sentence that states a fact.
3. If the sources do not contain the answer, set "answerable" to false and say briefly that you \
don't know, in the language of the question. Do not guess, and do not answer a related question instead.
4. Sources often describe DIFFERENT situations (e.g. university studies vs. a language course, \
before vs. after a given date, one scholarship programme vs. another). That is not a conflict: \
answer for the situation the question asks about, and if the question doesn't say which, briefly \
give each case. Only when two sources give different values for the SAME thing in the SAME situation \
is it a conflict: then give the value from the most recent source (see each source's date), cite it, \
and mention that an older source gives a different figure. Never let one source "override" another \
that is about a different situation.
5. If a source's information is clearly tied to a past date or campaign, say so.
6. Answer in the language of the question (French or English), concisely: 1-4 sentences, or a short \
list when the question asks for several items.

Return JSON with:
- "answer": the answer text with [S#] citations
- "answerable": true if the sources answer the question, false otherwise
- "sources_used": the list of source labels you cited, e.g. ["S1", "S3"]"""

# Worked examples, appended to the instructions. They teach the rules the small model
# breaks most (newest source for the same thing, no unsupported extras, "I don't
# know"), and they lift the fixed prefix above the 1,024 tokens OpenAI needs before
# it caches a prompt. The sources are invented so no eval answer leaks into the prompt.
EXAMPLES = """

Examples (invented sources, for illustration only):

Example 1. Two sources give different values for the same thing in the same situation.
Sources:
[S1] Visa guide | Embassy of Examplia | published: 2021-03-02
Applicants must show 850 EUR per month on a blocked account.
[S2] Student visa FAQ | Examplia Foreign Office | published: 2025-01-15
From 1 January 2025, the blocked account must hold 950 EUR per month (11,400 EUR per year).
Question: How much money do I need on the blocked account?
Output: {"answer": "You need 950 EUR per month, i.e. 11,400 EUR per year, on the blocked account [S2]. An older 2021 guide gives 850 EUR per month, but that figure has been replaced [S1].", "answerable": true, "sources_used": ["S2", "S1"]}

Example 2. Two sources describe different situations: this is not a conflict.
Sources:
[S1] Fees | Example University | published: 2025-09-01
Tuition for non-EU students in a Master's programme is 3,000 EUR per year.
[S2] Language centre | Example University | published: unknown
The intensive language course costs 1,200 EUR per semester.
Question: Combien coûtent les frais d'inscription en master ?
Output: {"answer": "Les frais d'inscription en master sont de 3 000 EUR par an pour les étudiants non européens [S1].", "answerable": true, "sources_used": ["S1"]}
(The language course is a different situation, so it is not mentioned.)

Example 3. Each sentence states only what its cited source says, with no added detail.
Sources:
[S1] Work rules | Examplia Immigration | published: 2024-06-10
Students may work up to 20 hours per week during term and full time during scheduled breaks.
Question: Can I work while studying?
Output: {"answer": "Yes: up to 20 hours per week during term, and full time during scheduled breaks [S1].", "answerable": true, "sources_used": ["S1"]}
(Not added: rules about work permits, salaries or other countries, because S1 does not state them.)

Example 4. The sources do not answer the question.
Sources:
[S1] Housing | Example University | published: 2025-02-01
Students can apply for a room in the residence halls from 1 May.
Question: Quelle est la date limite pour candidater à la bourse ?
Output: {"answer": "Je ne sais pas : les sources disponibles ne donnent pas la date limite de candidature à la bourse.", "answerable": false, "sources_used": []}

Example 5. The only source is tied to a past campaign.
Sources:
[S1] Call for applications 2023-2024 | Examplia Scholarship Agency | published: 2022-11-20
Applications for the 2023-2024 Examplia Excellence Scholarship close on 15 January 2023. The scholarship pays 1,000 EUR per month for up to 24 months.
Question: When is the deadline for the Examplia Excellence Scholarship?
Output: {"answer": "The last call found was for 2023-2024, and it closed on 15 January 2023 [S1]. That date belongs to a past campaign, so check the agency's website for the current deadline.", "answerable": true, "sources_used": ["S1"]}
(The monthly amount is not mentioned because the question does not ask for it.)"""


SCHEMA = {
    "type": "object",
    "properties": {
        "answer": {"type": "string"},
        "answerable": {"type": "boolean"},
        "sources_used": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["answer", "answerable", "sources_used"],
    "additionalProperties": False,
}


@dataclass
class Answer:
    question: str
    answer: str
    answerable: bool
    citations: list          # [{"label", "chunk_id", "title", "url", "published"}] for cited sources
    sources: list            # every chunk shown to the model, in order
    usage: dict = field(default_factory=dict)
    cost_usd: float = 0.0
    latency_s: dict = field(default_factory=dict)


MAX_ATTEMPTS = 2  # one retry if the answer slips into another script

# Small models occasionally drop a word from another script into a French or English
# answer (seen: Hindi "अलग" inside a French sentence). Any of these scripts in the
# answer but not in the question triggers a retry.
# Greek, Cyrillic, Hebrew, Indic, Thai/Tibetan, Hangul, Japanese kana, CJK.
OTHER_SCRIPTS = re.compile(
    r"[Ͱ-ϿЀ-ӿ֐-׿ऀ-෿฀-࿿"
    r"ᄀ-ᇿ぀-ヿ㐀-鿿가-힯]"
)


def foreign_script(answer, question):
    return bool(OTHER_SCRIPTS.search(answer)) and not OTHER_SCRIPTS.search(question)


FRENCH_HINTS = set("le la les des du un une est et pour que qui dans sur avec quel quelle quels quelles "
                   "combien comment puis-je puis je faut-il faut il elle mon ma mes vous votre en au aux "
                   "ce cette pas ou où être avoir dois peut peux".split())
ENGLISH_HINTS = set("the a an is are and for that which in on with what how much many can do does "
                    "i my you your to of need be have must".split())


def question_language(question):
    """French or English, from accents and common words (good enough for these two)."""
    words = question.lower().replace("?", " ").replace("'", " ").replace("’", " ").split()
    french = sum(w in FRENCH_HINTS for w in words) + 2 * any(c in question for c in "éèêàçùôîÉ")
    english = sum(w in ENGLISH_HINTS for w in words)
    return "French" if french > english else "English"


def newest_first(chunks):
    """Reorder the dated chunks newest first, among the slots they already hold; undated
    chunks keep their reranker position. Small models lean on [S1], so when two dated
    sources disagree this puts the current figure where the model looks first."""
    slots = [i for i, c in enumerate(chunks) if c.get("published")]
    dated = sorted((chunks[i] for i in slots), key=lambda c: c["published"], reverse=True)
    out = list(chunks)
    for i, c in zip(slots, dated):
        out[i] = c
    return out


def format_sources(chunks):
    blocks = []
    for i, c in enumerate(chunks, 1):
        header = f"[S{i}] {c['title']} | {c['publisher']} | published: {c.get('published') or 'unknown'}"
        if c.get("page"):
            header += f" | page {c['page']}"
        blocks.append(f"{header}\n{c['text']}")
    return "\n\n".join(blocks)


def cost(model, usage):
    price_in, price_cached, price_out = PRICES.get(model, (0, 0, 0))
    cached = usage.get("cached_input_tokens", 0)
    fresh = usage.get("input_tokens", 0) - cached
    return (fresh * price_in + cached * price_cached + usage.get("output_tokens", 0) * price_out) / 1e6


class Librarian:
    def __init__(self, model=MODEL, top_k=TOP_K, retriever=None, rerank=True, effort=EFFORT,
                 examples=USE_EXAMPLES, newest=NEWEST_FIRST):
        self.model, self.top_k, self.rerank, self.effort = model, top_k, rerank, effort
        self.instructions = INSTRUCTIONS + EXAMPLES if examples else INSTRUCTIONS
        self.newest = newest
        self.retriever = retriever or Retriever()
        self.client = OpenAI()

    def ask(self, question, **filters):
        t0 = time.perf_counter()
        chunks = self.retrieve(question, **filters)
        return self.answer_from(question, chunks, retrieval_s=time.perf_counter() - t0)

    def retrieve(self, question, **filters):
        """Step 1: the chunks the model will read."""
        hits = self.retriever.search(question, k=self.top_k, rerank=self.rerank, **filters)
        return [h.chunk for h in hits]

    def answer_from(self, question, chunks, retrieval_s=0.0):
        """Step 2: write the cited answer from those chunks."""
        t1 = time.perf_counter()
        if self.newest:
            chunks = newest_first(chunks)
        usage = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "reasoning_tokens": 0}
        for attempt in range(MAX_ATTEMPTS):
            response = self.client.responses.create(
                model=self.model,
                instructions=self.instructions,
                # Same key for every request, so they reach a server holding the cached prefix.
                prompt_cache_key="librarian",
                input=(f"Sources:\n\n{format_sources(chunks)}\n\nQuestion: {question}\n\n"
                       f"Write the answer in {question_language(question)}."),
                reasoning={"effort": self.effort},
                text={"format": {"type": "json_schema", "name": "answer", "schema": SCHEMA, "strict": True}},
            )
            u = response.usage  # every attempt is paid for, so every attempt is counted
            usage["input_tokens"] += u.input_tokens
            usage["cached_input_tokens"] += getattr(u.input_tokens_details, "cached_tokens", 0) or 0
            usage["output_tokens"] += u.output_tokens
            usage["reasoning_tokens"] += getattr(u.output_tokens_details, "reasoning_tokens", 0) or 0
            data = json.loads(response.output_text)
            if not foreign_script(data["answer"], question):
                break
        usage["attempts"] = attempt + 1
        t2 = time.perf_counter()

        labels = {f"S{i}": c for i, c in enumerate(chunks, 1)}
        citations = [{"label": s, "chunk_id": labels[s]["chunk_id"], "title": labels[s]["title"],
                      "url": labels[s]["url"], "published": labels[s].get("published"),
                      "publisher": labels[s]["publisher"], "country": labels[s]["country"],
                      "page": labels[s].get("page")}
                     for s in data["sources_used"] if s in labels]
        return Answer(
            question=question,
            answer=data["answer"],
            answerable=data["answerable"],
            citations=citations,
            sources=[c["chunk_id"] for c in chunks],
            usage=usage,
            cost_usd=cost(self.model, usage),
            latency_s={"retrieval": retrieval_s, "generation": t2 - t1, "total": retrieval_s + t2 - t1},
        )
