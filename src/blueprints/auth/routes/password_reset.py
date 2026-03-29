from __future__ import annotations

from flask import request, render_template, redirect, url_for, flash

from .. import auth_bp
from ....usecases.auth.reset_password import reset_password_usecase

@auth_bp.route("/password-reset", methods=["GET"])
def password_reset_view():
    return render_template("auth/password_reset.html")

@auth_bp.route("/password-reset", methods=["POST"])
def password_reset_process():
    email = request.form.get("email", "")
    new_password1 = request.form.get("new_password1", "")
    new_password2 = request.form.get("new_password2", "")

    result = reset_password_usecase(email=email, new_password1=new_password1, new_password2=new_password2)

    if not result.ok:
        flash(result.message, "エラー")
        return redirect(url_for("auth.password_reset_view"))

    flash("パスワード再設定が完了しました", "正常")
    return redirect(url_for("auth.login_view"))
