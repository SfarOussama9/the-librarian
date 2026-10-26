"""Tokenizer for keyword search over French and English text."""

import re
import unicodedata

# Function words in French and English that carry no meaning for search.
STOPWORDS = set("""
a an and are as at be been but by can do does for from had has have how i if in into is it its
may must my no not of on or our should so such than that the their them then there these they
this to was we were what when where which who why will with would you your
au aux avec ce ces cet cette dans de des du elle en est et etre eux il ils je la le les leur
leurs lui ma mais me mes mon ne nos notre nous on ou par pas pour qu que qui sa se ses son sur
ta te tes ton tu un une vos votre vous y d l s n c j m t qu
""".split())

TOKEN = re.compile(r"[a-z0-9]+")


def fold(text):
    """Lowercase and strip accents, so "Étudiant" and "etudiant" match."""
    text = unicodedata.normalize("NFKD", text.lower())
    return "".join(c for c in text if not unicodedata.combining(c))


def tokenize(text):
    return [t for t in TOKEN.findall(fold(text)) if t not in STOPWORDS]
