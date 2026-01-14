from __future__ import annotations

from .._result import Result
from ..validators import is_valid_email
from ...extensions import db


def update_profile_usecase(*, user, new_username: str, new_email: str) -> Result[None]:
    if new_username == "" or new_email == "":
        return Result.failure("空のフォームがあります")
    if not is_valid_email(new_email):
        return Result.failure("メールアドレスの形式になっていません")

    try:
        user.username = new_username
        user.email = new_email
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    finally:
        db.session.close()

    return Result.success()
