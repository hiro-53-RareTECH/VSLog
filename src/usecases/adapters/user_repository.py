from __future__ import annotations
from ...models.users import User

def get_by_email(email: str) -> User | None:
    return User.select_by_email(email)
