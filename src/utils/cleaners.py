import re

_RE_HTML        = re.compile(r"<[^>]+>")
_RE_URL         = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)
_RE_PUNCTUATION = re.compile(r"[^\w\s\u0600-\u06FF]")
_RE_NUMBERS     = re.compile(r"\b\d+\b")
_RE_WHITESPACE  = re.compile(r"\s+")
_RE_TATWEEL     = re.compile(r"\u0640+")
_RE_TASHKEEL    = re.compile(
    r"[\u064B-\u065F\u0670]"
)

# --- Arabic normalization maps ---
_ALEF_MAP = str.maketrans(
    "\u0622\u0623\u0625\u0671",
    "\u0627\u0627\u0627\u0627",
)
_HAMZA_MAP = str.maketrans(
    "\u0624\u0626",
    "\u0621\u0621",
)
_TEH_MARBUTA_MAP = str.maketrans("\u0629", "\u0647")


# --- Shared cleaners ---
def remove_html_tags(text: str) -> str:
    return _RE_HTML.sub(" ", text)

def remove_urls(text: str) -> str:
    return _RE_URL.sub(" ", text)

def remove_punctuation(text: str) -> str:
    return _RE_PUNCTUATION.sub(" ", text)

def remove_numbers(text: str) -> str:
    return _RE_NUMBERS.sub(" ", text)

def collapse_whitespace(text: str) -> str:
    return _RE_WHITESPACE.sub(" ", text).strip()


# --- Arabic specific ---
def remove_tashkeel(text: str) -> str:
    return _RE_TASHKEEL.sub("", text)

def remove_tatweel(text: str) -> str:
    return _RE_TATWEEL.sub("", text)

def normalize_alef(text: str) -> str:
    return text.translate(_ALEF_MAP)

def normalize_hamza(text: str) -> str:
    return text.translate(_HAMZA_MAP)

def normalize_teh_marbuta(text: str) -> str:
    return text.translate(_TEH_MARBUTA_MAP)