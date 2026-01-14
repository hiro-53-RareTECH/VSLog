from __future__ import annotations

import uuid

from .._result import Result
from ..validators import is_valid_email, is_valid_password
from ..adapters import get_by_email, hash_password
from ...extensions import db
from ...models.users import User
from ..auth.login import LoginOutput

def signup_usecase(*, username: str, email: str, password1: str, password2: str) -> Result[LoginOutput]:
    if username == "" or email == "" or password1 == "" or password2 == "":
        return Result.failure("ユーザー名、メールアドレス、パスワードのいずれかが空です")
    if password1 != password2:
        return Result.failure("パスワードが一致しません")
    if not is_valid_email(email):
        return Result.failure("メールアドレスの形式になっていません")
    if not is_valid_password(password1):
        return Result.failure("パスワードは8文字以上16文字以内で入力してください")

    if get_by_email(email) is not None:
        return Result.failure("既に登録されているメールアドレスです")

    user = User(
        user_id=uuid.uuid4(),
        username=username,
        email=email,
        password=hash_password(password1),
    )

    try:
        db.session.add(user)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise
    finally:
        db.session.close()

    new_user = get_by_email(email)
    return Result.success(LoginOutput(user=new_user))
