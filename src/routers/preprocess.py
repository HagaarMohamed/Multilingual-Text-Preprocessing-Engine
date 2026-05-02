import logging
from fastapi import APIRouter, HTTPException, status
from src.models.schemas import PreprocessRequest, PreprocessResponse
from src.services.english_service import preprocess_english
from src.services.arabic_service import preprocess_arabic

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["preprocessing"])

@router.post("/preprocess", response_model=PreprocessResponse)
def preprocess(req: PreprocessRequest) -> PreprocessResponse:

    # Error 1: empty text
    if not req.text.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Input text is empty.",
        )

    # Error 2: language mismatch
    ar_chars = sum(1 for c in req.text if "\u0600" <= c <= "\u06FF")
    en_chars = sum(1 for c in req.text if c.isascii() and c.isalpha())

    if req.language == "ar" and ar_chars == 0 and en_chars > 5:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Language mismatch: text looks English but Arabic selected.",
        )

    # Dispatch to correct service
    if req.language == "en":
        processed, steps = preprocess_english(req)
    else:
        processed, steps = preprocess_arabic(req)

    # Log the request
    logger.info(f"Language: {req.language} | Tokens before: {len(req.text.split())} | Tokens after: {len(processed.split())}")

    return PreprocessResponse(
        original_text=req.text,
        processed_text=processed,
        language=req.language,
        steps_applied=steps,
        token_count_before=len(req.text.split()),
        token_count_after=len(processed.split()) if processed.strip() else 0,
    )

@router.get("/health")
def health():
    return {"status": "ok"}