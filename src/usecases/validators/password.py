from __future__ import annotations
import re

PASSWORD_PATTERN = r"^.{8,16}$"

def is_valid_password(password: str) -> bool:
    return re.match(PASSWORD_PATTERN, password) is not None
