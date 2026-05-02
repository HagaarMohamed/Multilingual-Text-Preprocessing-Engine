import pyarabic.araby as araby

from src.config.settings import ARABIC_STOPWORDS, MIN_TOKEN_LENGTH
from src.models.schemas import PreprocessRequest
from src.utils.cleaners import (
    remove_html_tags, remove_urls, remove_punctuation,
    remove_numbers, collapse_whitespace,
    remove_tashkeel, remove_tatweel,
    normalize_alef, normalize_hamza, normalize_teh_marbuta,
)

def preprocess_arabic(req: PreprocessRequest) -> tuple[str, list[str]]:
    text = req.text
    steps = []

    if req.remove_html:
        text = remove_html_tags(text)
        steps.append("Removed HTML tags")

    if req.remove_urls:
        text = remove_urls(text)
        steps.append("Removed URLs")

    if req.remove_tashkeel:
        text = araby.strip_tashkeel(text)
        text = remove_tashkeel(text)
        steps.append("Removed tashkeel")

    if req.remove_tatweel:
        text = araby.strip_tatweel(text)
        text = remove_tatweel(text)
        steps.append("Removed tatweel")

    if req.normalize_alef:
        text = araby.normalize_alef(text)
        text = normalize_alef(text)
        steps.append("Normalised Alef")

    if req.normalize_hamza:
        text = araby.normalize_hamza(text)
        text = normalize_hamza(text)
        steps.append("Normalised Hamza")

    if req.normalize_teh_marbuta:
        text = normalize_teh_marbuta(text)
        steps.append("Normalised Teh Marbuta")

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
            if t not in ARABIC_STOPWORDS and len(t) >= MIN_TOKEN_LENGTH
        ]
        steps.append(f"Removed stopwords ({before - len(tokens)} words filtered)")

    if req.lowercase:
        tokens = [t.lower() for t in tokens]
        steps.append("Lowercased")

    # BUG FIX 
    processed = " ".join(tokens)

    if req.remove_extra_whitespace:
        processed = collapse_whitespace(processed)
        steps.append("Normalised whitespace")

    return processed, steps