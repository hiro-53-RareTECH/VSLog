from __future__ import annotations

from flask import redirect, url_for, flash
from flask_login import logout_user

from .. import auth_bp


@auth_bp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    flash("ログアウトしました", "正常")
    return redirect(url_for("auth.login_view"))
