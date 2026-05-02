# src/services/english_service.py
import nltk
from nltk.stem import PorterStemmer

from src.config.settings import ENGLISH_STOPWORDS, MIN_TOKEN_LENGTH
from src.models.schemas import PreprocessRequest
from src.utils.cleaners import (
    remove_html_tags, remove_urls, remove_punctuation,
    remove_numbers, collapse_whitespace,
)

# (loaded once not every time, reused)
_stemmer = None
_nlp = None
def _get_stemmer():
    global _stemmer
    if _stemmer is None:
        _stemmer = PorterStemmer()
    return _stemmer

def _get_nlp():
    global _nlp
    if _nlp is None:
        import spacy
        _nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    return _nlp
def preprocess_english(req: PreprocessRequest) -> tuple[str, list[str]]:
    text = req.text
    steps = []

    if req.remove_html:
        text = remove_html_tags(text)
        steps.append("Removed HTML tags")

    if req.remove_urls:
        text = remove_urls(text)
        steps.append("Removed URLs")

    
    if req.lowercase:
        text = text.lower()
        steps.append("Lowercased")

    if req.remove_punctuation:
        text = remove_punctuation(text)
        steps.append("Removed punctuation")

    if req.remove_numbers:
        text = remove_numbers(text)
        steps.append("Removed numbers")

    text = collapse_whitespace(text)

    tokens = text.split()

    if req.remove_stopwords:
        before = len(tokens)
        tokens = [
            t for t in tokens
            if t not in ENGLISH_STOPWORDS and len(t) >= MIN_TOKEN_LENGTH
        ]
        steps.append(f"Removed stopwords ({before - len(tokens)} words filtered)")

    if req.lemmatize and not req.stemming:
        nlp = _get_nlp()
        doc = nlp(" ".join(tokens))
        tokens = [token.lemma_ for token in doc]
        steps.append("Lemmatized (spaCy)")

    elif req.stemming and not req.lemmatize:
        stemmer = _get_stemmer()
        tokens = [stemmer.stem(t) for t in tokens]
        steps.append("Stemmed (Porter)")

    # 9. BUG FIX
    processed = " ".join(tokens)

    if req.remove_extra_whitespace:
        processed = collapse_whitespace(processed)
        steps.append("Normalised whitespace")

    return processed, steps