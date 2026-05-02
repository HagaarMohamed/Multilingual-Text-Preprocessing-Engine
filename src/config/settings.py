ENGLISH_STOPWORDS = {
    "i", "me", "my", "we", "our", "you", "your", "he", "him", "his",
    "she", "her", "it", "its", "they", "them", "what", "which", "who",
    "this", "that", "these", "those", "am", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did",
    "a", "an", "the", "and", "but", "if", "or", "as", "of", "at", "by",
    "for", "with", "about", "into", "through", "before", "after", "to",
    "from", "up", "down", "in", "out", "on", "off", "then", "once",
    "here", "there", "when", "where", "why", "how", "all", "both",
    "no", "not", "only", "same", "so", "than", "too", "very", "just",
    "can", "will", "don", "should", "now",
}

ARABIC_STOPWORDS = {
    "في", "من", "إلى", "على", "عن", "مع", "هذا", "هذه", "ذلك", "تلك",
    "التي", "الذي", "الذين", "كان", "كانت", "هو", "هي", "هم", "هن",
    "أنا", "نحن", "أنت", "أنتم", "لكن", "لأن", "حتى", "إذا", "ثم",
    "أو", "و", "ف", "ب", "ل", "لا", "ما", "لم", "لن", "قد",
    "كل", "بعض", "أي", "كيف", "متى", "أين", "لماذا", "هل",
    "إن", "أن", "كما", "عند", "بعد", "قبل", "بين", "خلال",
    "تحت", "فوق", "أمام", "يمكن", "يجب", "ليس", "ليست",
    "أيضا", "فقط", "جدا", "هناك", "هنا", "الآن", "اليوم",
}

MIN_TOKEN_LENGTH = 2