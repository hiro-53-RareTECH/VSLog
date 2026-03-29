from __future__ import annotations

from .._result import Result
from ..validators import is_valid_email, is_valid_password
from ..adapters import get_by_email, hash_password
from ...extensions import db

def reset_password_usecase(*, email: str, new_password1: str, new_password2: str) -> Result[None]:
    if email == "" or new_password1 == "" or new_password2 == "":
        return Result.failure("空のフォームがあります")
    if new_password1 != new_password2:
        return Result.failure("パスワードが一致しません")
    if not is_valid_email(email):
        return Result.failure("メールアドレスの形式になっていません")
    if not is_valid_password(new_password1):
        return Result.failure("パスワードは8文字以上16文字以内で入力してください")

    user = get_by_email(email)
    if user is None:
        return Result.failure("登録されていないメールアドレスです")

    try:
        user.password = hash_password(new_password1)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    finally:
        db.session.close()

    return Result.success()
