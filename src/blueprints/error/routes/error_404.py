from flask import render_template

from .. import error_bp

@error_bp.errorhandler(404)
def page_not_found(e):
    return render_template('error.404.html')