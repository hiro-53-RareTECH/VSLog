from __future__ import annotations

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user

from .. import auth_bp
from ....usecases.auth.signup import signup_usecase

@auth_bp.route("/signup", methods=["GET"])
def signup_view():
    return render_template("auth/signup.html")

@auth_bp.route("/signup", methods=["POST"])
def signup_process():
    username = request.form.get("username", "")
    email = request.form.get("email", "")
    password1 = request.form.get("password1", "")
    password2 = request.form.get("password2", "")

    result = signup_usecase(username=username, email=email, password1=password1, password2=password2)

    if not result.ok:
        flash(result.message, "エラー")
        return redirect(url_for("auth.signup_view"))

    login_user(result.value.user)
    flash("ログインしました", "正常")
    return redirect(url_for("study.dashboard_view", user_id=str(result.value.user.user_id)))
