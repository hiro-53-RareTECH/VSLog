from flask import render_template

from .. import error_bp

@error_bp.errorhandler(403)
def page_forbidden(e):
    return render_template('error/403.html'), 403
