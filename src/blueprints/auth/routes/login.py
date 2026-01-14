from __future__ import annotations

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user

from .. import auth_bp
from ....usecases.auth.login import login_usecase

@auth_bp.route("/login", methods=["GET"])
def login_view():
    return render_template("auth/login.html")

@auth_bp.route("/login", methods=["POST"])
def login_process():
    email = request.form.get("email", "")
    password = request.form.get("password", "")

    result = login_usecase(email=email, password=password)

    if not result.ok:
        flash(result.message, "エラー")
        return redirect(url_for("auth.login_view"))

    login_user(result.value.user)
    flash("ログインしました", "正常")
    return redirect(url_for("study.dashboard_view", user_id=str(result.value.user.user_id)))
