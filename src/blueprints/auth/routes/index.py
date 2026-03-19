from flask import render_template

from .. import auth_bp

@auth_bp.route("/", methods=["GET"])
def index_view():
    return render_template("auth/index.html")
