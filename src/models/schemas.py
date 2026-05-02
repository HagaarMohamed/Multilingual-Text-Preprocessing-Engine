from typing import Literal
from pydantic import BaseModel, Field


class PreprocessRequest(BaseModel):
    # Required fields
    text: str = Field(..., min_length=1, description="Input text to preprocess")
    language: Literal["en", "ar"] = Field(..., description="'en' or 'ar'")

    # Shared toggles
    lowercase: bool = Field(True)
    remove_html: bool = Field(True)
    remove_urls: bool = Field(True)
    remove_punctuation: bool = Field(True)
    remove_numbers: bool = Field(False)
    remove_stopwords: bool = Field(True)
    remove_extra_whitespace: bool = Field(True)

    # English only
    lemmatize: bool = Field(False)
    stemming: bool = Field(False)

    # Arabic only
    remove_tashkeel: bool = Field(True)
    remove_tatweel: bool = Field(True)
    normalize_alef: bool = Field(True)
    normalize_hamza: bool = Field(True)
    normalize_teh_marbuta: bool = Field(False)


class PreprocessResponse(BaseModel):
    original_text: str
    processed_text: str
    language: str
    steps_applied: list[str]
    token_count_before: int
    token_count_after: int