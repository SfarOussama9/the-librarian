// AbroadGuide page: ask, show progress, render the cited answer and its source stamps.

const TEXT = {
  fr: {
    brand: "Le Bibliothécaire",
    brandSub: "Études à l'étranger, sources officielles",
    headline: "Posez votre question sur les études en France, en Allemagne, au Canada ou avec Erasmus+.",
    label: "Votre question",
    placeholder: "Par exemple : documents pour le visa étudiant allemand",
    ask: "Demander",
    asking: "Recherche…",
    try: "Essayez :",
    stepSearch: "Recherche dans 281 documents officiels",
    stepWrite: "Rédaction de la réponse à partir des meilleurs passages",
    feedbackQ: "Cette réponse vous a-t-elle aidé ?",
    useful: "Oui, utile",
    notUseful: "Non, erronée ou floue",
    commentLabel: "Qu'est-ce qui n'allait pas ? (facultatif)",
    send: "Envoyer l'avis",
    thanks: "Merci, votre avis est enregistré.",
    footer1: "Réponses tirées de 281 documents officiels (Campus France, ambassade d'Allemagne, DAAD, IRCC, Commission européenne…) collectés en octobre 2026. Vérifiez toujours auprès de l'organisme concerné avant une démarche.",
    footer2: "Les questions et les avis sont enregistrés de façon anonyme pour améliorer le service. Projet CS496, MedTech.",
    published: "Publié le",
    undated: "Date non indiquée",
    page: "page",
    pdf: "Document PDF",
    you: "Votre question :",
    errFailed: "La réponse n'a pas pu être générée. Réessayez dans un instant.",
    errVisitor: "Limite atteinte : 20 questions par heure. Réessayez un peu plus tard.",
    errDaily: "Le service a atteint sa limite de questions pour aujourd'hui. Réessayez demain.",
    errNetwork: "Connexion au serveur impossible. Vérifiez votre connexion et réessayez.",
    countries: { france: "France", germany: "Allemagne", canada: "Canada", erasmus: "Erasmus+" },
  },
  en: {
    brand: "AbroadGuide",
    brandSub: "Studying abroad, official sources",
    headline: "Ask about studying in France, Germany, Canada or with Erasmus+.",
    label: "Your question",
    placeholder: "For example: documents for a German student visa",
    ask: "Ask",
    asking: "Searching…",
    try: "Try:",
    stepSearch: "Searching 281 official documents",
    stepWrite: "Writing the answer from the best passages",
    feedbackQ: "Did this answer help?",
    useful: "Yes, useful",
    notUseful: "No, wrong or unclear",
    commentLabel: "What was wrong? (optional)",
    send: "Send feedback",
    thanks: "Thanks, your feedback is saved.",
    footer1: "Answers come from 281 official documents (Campus France, German embassy, DAAD, IRCC, European Commission…) collected in October 2026. Always check with the organisation concerned before you act.",
    footer2: "Questions and feedback are saved anonymously to improve the service. CS496 project, MedTech.",
    published: "Published",
    undated: "Date not given",
    page: "page",
    pdf: "PDF document",
    you: "Your question:",
    errFailed: "The answer could not be generated. Try again in a moment.",
    errVisitor: "Limit reached: 20 questions per hour. Try again a little later.",
    errDaily: "The service has reached today's question limit. Try again tomorrow.",
    errNetwork: "Can't reach the server. Check your connection and try again.",
    countries: { france: "France", germany: "Germany", canada: "Canada", erasmus: "Erasmus+" },
  },
};

const $ = (s) => document.querySelector(s);
let lang = "fr";
let currentAnswerId = null;
let busy = false;

// ---------- language ----------
function setLang(next) {
  lang = next;
  document.documentElement.lang = next;
  document.title = TEXT[next].brand;
  document.querySelectorAll("[data-i18n]").forEach((el) => { el.textContent = TEXT[next][el.dataset.i18n]; });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => { el.placeholder = TEXT[next][el.dataset.i18nPlaceholder]; });
  document.querySelectorAll(".lang button").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.lang === next)));
  try { localStorage.setItem("librarian-lang", next); } catch (_) { /* storage blocked: keep default */ }
}

// ---------- guilloché band ----------
function drawGuilloche() {
  const svg = $("#guilloche");
  const w = 1200, h = 72;
  svg.setAttribute("viewBox", `0 0 ${w} ${h}`);
  let paths = "";
  for (let k = 0; k < 14; k++) {
    let d = "";
    for (let x = 0; x <= w; x += 6) {
      const y = h / 2
        + Math.sin(x / 38 + k * 0.45) * (14 + k * 0.9)
        + Math.sin(x / 11 + k * 1.3) * 3.2;
      d += (x === 0 ? "M" : "L") + x + " " + y.toFixed(1) + " ";
    }
    paths += `<path d="${d}"/>`;
  }
  svg.innerHTML = paths;
}

// ---------- rendering ----------
const escapeHtml = (s) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

function shortPublisher(p) {
  return p.replace(/\s*\(.*?\)\s*/g, " ").trim()
    .replace("Immigration, Refugees and Citizenship Canada", "IRCC")
    .replace("European Commission", lang === "fr" ? "Commission européenne" : "European Commission")
    .replace("DAAD Scholarship Database", "DAAD");
}

// PDF metadata titles are often junk ("Présentation PowerPoint", "Deutsche Botschaft Öffnungszeiten:").
const JUNK_TITLE = /PowerPoint|Öffnungszeiten|^Microsoft|^Untitled|^Document\d*$|:\s*$/i;
function stampTitle(c) {
  const title = !c.title || JUNK_TITLE.test(c.title) ? TEXT[lang].pdf : c.title;
  return c.page ? `${title}, ${TEXT[lang].page} ${c.page}` : title;
}

function formatDate(iso) {
  if (!iso) return TEXT[lang].undated;
  const d = new Date(iso + "T00:00:00");
  return `${TEXT[lang].published} ${new Intl.DateTimeFormat(lang === "fr" ? "fr-FR" : "en-GB", { day: "numeric", month: "short", year: "numeric" }).format(d)}`;
}

// Turn the model's text (light Markdown + [S1] marks) into safe HTML.
function renderAnswer(text, numbers, colours) {
  const cite = (label) => {
    const n = numbers[label];
    return n ? `<a class="cite" href="#stamp-${n}" style="background:${colours[label]}" aria-label="source ${n}">${n}</a>` : "";
  };
  const inline = (s) => escapeHtml(s)
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/((?:\[S\d+\])+)/g, (group) => {
      const seen = new Set();
      return (group.match(/S\d+/g) || []).filter((l) => numbers[l] && !seen.has(numbers[l]) && seen.add(numbers[l])).map(cite).join("");
    });
  const blocks = [];
  let list = [];
  const flush = () => { if (list.length) { blocks.push(`<ul>${list.map((li) => `<li>${inline(li)}</li>`).join("")}</ul>`); list = []; } };
  for (const line of text.split(/\n+/)) {
    const m = line.match(/^\s*[-•*]\s+(.*)/);
    if (m) { list.push(m[1]); continue; }
    flush();
    if (line.trim()) blocks.push(`<p>${inline(line.trim())}</p>`);
  }
  flush();
  return blocks.join("");
}

const INK = {
  france: "var(--stamp-france)", germany: "var(--stamp-germany)",
  canada: "var(--stamp-canada)", erasmus: "var(--stamp-erasmus)",
};
const TILTS = [-2.5, 1.8, -1.2, 2.6];

function showResult(data) {
  // One stamp per document page: passages cited from the same page share a stamp and a number.
  const numbers = {}, colours = {}, docs = [];
  (data.answerable ? data.citations : []).forEach((c) => {
    const key = `${c.url}#${c.page || ""}`;
    let n = docs.findIndex((d) => d.key === key) + 1;
    if (!n) { docs.push({ key, ...c }); n = docs.length; }
    numbers[c.label] = n;
    colours[c.label] = INK[c.country] || "var(--ink)";
  });

  const answer = $("#answer");
  answer.className = "answer" + (data.answerable ? "" : " unknown");
  answer.innerHTML = renderAnswer(data.answer, numbers, colours);

  const stamps = $("#stamps");
  stamps.innerHTML = "";
  // A refusal has no source that answers it, so it gets no stamps (docs is empty).
  docs.forEach((c, i) => {
    const a = document.createElement("a");
    a.className = "stamp";
    a.id = `stamp-${i + 1}`;
    a.href = c.url;
    a.target = "_blank";
    a.rel = "noopener";
    a.dataset.country = c.country;
    a.style.setProperty("--tilt", `${TILTS[i % TILTS.length]}deg`);
    a.innerHTML = `
      <span class="stamp-num" aria-hidden="true">${i + 1}</span>
      <span class="stamp-country">${escapeHtml(TEXT[lang].countries[c.country] || c.country)}</span>
      <span class="stamp-publisher">${escapeHtml(shortPublisher(c.publisher))}</span>
      <span class="stamp-title">${escapeHtml(stampTitle(c))}</span>
      <span class="stamp-date">${escapeHtml(formatDate(c.published))}</span>`;
    stamps.appendChild(a);
    // Press the stamps one after another.
    setTimeout(() => a.classList.add("pressed"), 120 * i);
  });

  currentAnswerId = data.answer_id;
  const fb = $("#feedback");
  fb.hidden = false;
  fb.querySelectorAll("[data-rating]").forEach((b) => { b.setAttribute("aria-pressed", "false"); b.disabled = false; });
  $("#comment-form").hidden = true;
  $("#comment").value = "";
  $("#thanks").hidden = true;
}

function showError(code) {
  const key = { visitor_limit: "errVisitor", daily_limit: "errDaily", network: "errNetwork" }[code] || "errFailed";
  $("#answer").className = "answer";
  $("#answer").innerHTML = `<p class="error">${escapeHtml(TEXT[lang][key])}</p>`;
}

function setStep(stage) {
  const p = $("#progress");
  const steps = [["search", TEXT[lang].stepSearch], ["write", TEXT[lang].stepWrite]];
  const at = steps.findIndex(([s]) => s === stage);
  p.innerHTML = steps.map(([s, label], i) =>
    `<div class="step ${i < at ? "done" : i === at ? "active" : ""}">${escapeHtml(label)}</div>`).join("");
}

// ---------- asking ----------
async function ask(question) {
  if (busy || question.trim().length < 3) return;
  busy = true;
  const button = $("#submit");
  button.disabled = true;
  button.textContent = TEXT[lang].asking;

  const result = $("#result");
  result.hidden = false;
  $("#asked").textContent = `${TEXT[lang].you} ${question}`;
  $("#answer").innerHTML = "";
  $("#stamps").innerHTML = "";
  $("#feedback").hidden = true;
  setStep("search");
  result.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });

  try {
    const res = await fetch("/api/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, lang }),
    });
    if (!res.ok) {
      const body = await res.json().catch(() => ({}));
      $("#progress").innerHTML = "";
      showError(body.error);
      return;
    }
    // Read the server-sent events as they arrive.
    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      let cut;
      while ((cut = buffer.indexOf("\n\n")) >= 0) {
        const raw = buffer.slice(0, cut);
        buffer = buffer.slice(cut + 2);
        const kind = (raw.match(/^event: (.*)$/m) || [])[1];
        const data = JSON.parse((raw.match(/^data: (.*)$/m) || [, "{}"])[1]);
        if (kind === "stage") setStep(data.stage);
        if (kind === "result") { $("#progress").innerHTML = ""; showResult(data); }
        if (kind === "error") { $("#progress").innerHTML = ""; showError(data.error); }
      }
    }
  } catch (_) {
    $("#progress").innerHTML = "";
    showError("network");
  } finally {
    busy = false;
    button.disabled = false;
    button.textContent = TEXT[lang].ask;
  }
}

async function sendFeedback(rating, comment = "") {
  if (!currentAnswerId) return;
  try {
    await fetch("/api/feedback", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answer_id: currentAnswerId, rating, comment }),
    });
  } catch (_) { /* feedback is best effort */ }
}

// ---------- wiring ----------
function autosize(t) { t.style.height = "auto"; t.style.height = t.scrollHeight + "px"; }

document.addEventListener("DOMContentLoaded", () => {
  drawGuilloche();
  window.addEventListener("resize", () => autosize($("#question")));
  if (document.fonts) document.fonts.ready.then(() => autosize($("#question")));
  let saved = null;
  try { saved = localStorage.getItem("librarian-lang"); } catch (_) { /* ignore */ }
  setLang(saved === "en" ? "en" : "fr");

  document.querySelectorAll(".lang button").forEach((b) => b.addEventListener("click", () => setLang(b.dataset.lang)));

  const q = $("#question");
  q.addEventListener("input", () => autosize(q));
  q.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); $("#ask").requestSubmit(); }
  });
  $("#ask").addEventListener("submit", (e) => { e.preventDefault(); ask(q.value.trim()); });

  document.querySelectorAll(".example").forEach((b) => b.addEventListener("click", () => {
    q.value = b.dataset.q; autosize(q); ask(b.dataset.q);
  }));

  document.querySelectorAll("[data-rating]").forEach((b) => b.addEventListener("click", () => {
    document.querySelectorAll("[data-rating]").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    if (b.dataset.rating === "up") {
      sendFeedback("up");
      document.querySelectorAll("[data-rating]").forEach((x) => { x.disabled = true; });
      $("#thanks").hidden = false;
    } else {
      $("#comment-form").hidden = false;
      $("#comment").focus();
    }
  }));
  // Shareable links: /?q=... asks that question on load.
  const shared = new URLSearchParams(location.search).get("q");
  if (shared) { q.value = shared; autosize(q); ask(shared); }

  $("#comment-form").addEventListener("submit", (e) => {
    e.preventDefault();
    sendFeedback("down", $("#comment").value.trim());
    $("#comment-form").hidden = true;
    document.querySelectorAll("[data-rating]").forEach((x) => { x.disabled = true; });
    $("#thanks").hidden = false;
  });
});
