from __future__ import annotations

from dataclasses import dataclass

from .._result import Result
from ..validators import is_valid_email, is_valid_password
from ..adapters import get_by_email, verify_password

@dataclass(frozen=True)
class LoginOutput:
    user: object

def login_usecase(*, email: str, password: str) -> Result[LoginOutput]:
    if email == "" or password == "":
        return Result.failure("空のフォームがあります")
    if not is_valid_email(email):
        return Result.failure("メールアドレスの形式になっていません")
    if not is_valid_password(password):
        return Result.failure("パスワードは8文字以上16文字以内で入力してください")

    user = get_by_email(email)
    if user is None:
        return Result.failure("登録されていないメールアドレスです")

    if not verify_password(user.password, password):
        return Result.failure("パスワードが違います")

    return Result.success(LoginOutput(user=user))
