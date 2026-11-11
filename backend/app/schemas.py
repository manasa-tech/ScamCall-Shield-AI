from typing import Literal
from pydantic import BaseModel, Field


class ScanRequest(BaseModel):
    content: str = Field(
        ...,
        min_length=3,
        max_length=10000
    )

    content_type: Literal[
        "url",
        "message",
        "email"
    ] = "message"


class ScanResponse(BaseModel):
    status: str
    risk_level: str
    risk_score: int
    explanation: str
    detected_urls: list[str]
    content_type: str
