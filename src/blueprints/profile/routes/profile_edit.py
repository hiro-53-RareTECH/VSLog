from __future__ import annotations

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from .. import profile_bp
from ....usecases.profile.update_profile import update_profile_usecase


@profile_bp.route("/profile-edit/<user_id>", methods=["GET"])
@login_required
def profile_edit_view(user_id: str):
    return render_template("profile/profile_edit.html")


@profile_bp.route("/profile-edit/<user_id>", methods=["POST"])
@login_required
def profile_edit_process(user_id: str):
    new_username = request.form.get("new_username", "")
    new_email = request.form.get("new_email", "")

    result = update_profile_usecase(user=current_user, new_username=new_username, new_email=new_email)

    if not result.ok:
        flash(result.message, "エラー")
        return redirect(url_for("profile.profile_edit_view", user_id=user_id))

    flash("プロフィール編集が完了しました", "正常")
    return redirect(url_for("profile.profile_edit_view", user_id=user_id))
