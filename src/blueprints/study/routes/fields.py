from flask import jsonify, redirect, render_template, request, url_for, abort
from flask_login import login_required, current_user

from .. import study_bp
from ....usecases.study.upsert_fields_bulk import upsert_fields_bulk_usecase

# 学習分野画面表示
@study_bp.route('/study-fields/<user_id>', methods=['GET'])
@login_required
def study_fields_view(user_id: str):
    if user_id != str(current_user.user_id):
        abort(403)
    return render_template('study/study_fields.html')

# 学習分野登録・編集・削除
@study_bp.route('/study-fields/<user_id>/', methods=['POST'])
@login_required
def study_fields_process(user_id: str):
    if user_id != str(current_user.user_id):
        return jsonify({'error': 'forbidden'}), 403
    upsert_fields_bulk_usecase(user_id=user_id, form=request.form)
    return redirect(url_for('study.study_fields_view', user_id=user_id))
