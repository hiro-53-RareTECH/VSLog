import pytest
from flask import url_for
from datetime import datetime, date

'''
1.学習履歴一覧画面にアクセスすると200のステータスコードが返ってくるか
2.
'''

def test_study_logs_list_view(app, auth_client, register_user):
    with app.test_request_context():
        url = url_for('study.study_logs_list_view', user_id=register_user['user_id'])
    res = auth_client.get(url)
    assert res.status_code == 200

    this_year = datetime.now().year
    this_month = datetime.now().month
    this_month_year = date(this_year, this_month, 1).strftime('%Y-%m')
    assert str(this_year) and str(this_month) and this_month_year in res.data.decode('utf-8')
