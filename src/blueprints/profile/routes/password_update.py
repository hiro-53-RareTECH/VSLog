from __future__ import annotations

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from .. import profile_bp
from ....usecases.profile.change_password import change_password_usecase


@profile_bp.route("/password-update/<user_id>", methods=["GET"])
@login_required
def password_update_view(user_id: str):
    return render_template("profile/password_update.html")


@profile_bp.route("/password-update/<user_id>", methods=["POST"])
@login_required
def password_update_process(user_id: str):
    current_password = request.form.get("current_password", "")
    new_password1 = request.form.get("new_password1", "")
    new_password2 = request.form.get("new_password2", "")

    result = change_password_usecase(
        user=current_user,
        current_password=current_password,
        new_password1=new_password1,
        new_password2=new_password2,
    )

    if not result.ok:
        flash(result.message, "エラー")
        return redirect(url_for("profile.password_update_view", user_id=user_id))

    flash("パスワード変更が完了しました", "正常")
    return redirect(url_for("profile.password_update_view", user_id=user_id))
