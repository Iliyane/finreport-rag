from __future__ import annotations

import os

from app.config import settings


def get_openai_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY") or settings.openai_api_key
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured.")
    return api_key
