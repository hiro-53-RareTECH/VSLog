from __future__ import annotations

from .._result import Result
from ..validators import is_valid_password
from ..adapters import verify_password, hash_password
from ...extensions import db
from ...models.users import User

def change_password_usecase(
    *,
    user_id,
    current_password: str,
    new_password1: str,
    new_password2: str,
) -> Result[None]:
    
    user = db.session.get(User, user_id)

    if current_password == "" or new_password1 == "" or new_password2 == "":
        return Result.failure("空のフォームがあります")
    if not verify_password(user.password, current_password):
        return Result.failure("現在のパスワードが正しくありません")
    if new_password1 != new_password2:
        return Result.failure("新しいパスワードと新しいパスワード（確認用）が一致しません")
    if not is_valid_password(new_password1):
        return Result.failure("パスワードは8文字以上16文字以内で入力してください")

    try:
        user.password = hash_password(new_password1)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise

    return Result.success()
