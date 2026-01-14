from __future__ import annotations
import re

EMAIL_PATTERN = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"

def is_valid_email(email: str) -> bool:
    return re.match(EMAIL_PATTERN, email) is not None
