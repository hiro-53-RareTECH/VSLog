from datetime import datetime

from flask import render_template, abort
from flask_login import login_required, current_user

from ..import study_bp

# ダッシュボード画面表示
@study_bp.route('/dashboard/<user_id>', methods=['GET'])
@login_required
def dashboard_view(user_id: str):
    if user_id != str(current_user.user_id):
        abort(403)
    this_year = datetime.now().year
    this_month = datetime.now().month

    return render_template(
        'study/dashboard.html',
        this_year=this_year,
        this_month=this_month
        )
