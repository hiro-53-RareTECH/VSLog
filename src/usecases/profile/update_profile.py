from __future__ import annotations

from .._result import Result
from ..validators import is_valid_email
from ...extensions import db
from ...models.users import User
from ..adapters import get_by_email

def update_profile_usecase(*, user_id, new_username: str, new_email: str) -> Result[None]:

    user = db.session.get(User, user_id)

    if new_username == "" or new_email == "":
        return Result.failure("空のフォームがあります")
    if not is_valid_email(new_email):
        return Result.failure("メールアドレスの形式になっていません")
    if get_by_email(new_email) is not None:
        return Result.failure("既に登録されているメールアドレスです")

    try:
        user.username = new_username
        user.email = new_email
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

    return Result.success()
