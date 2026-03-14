import pytest
from flask import url_for
from datetime import datetime

'''
1.ダッシュボード画面にアクセスして200のステータスコードが返ってくるか
2.this_year, this_monthのレスポンスがあるか
'''

def test_dashboard_view(app, register_user, auth_client):
    with app.test_request_context():
        url = url_for('study.dashboard_view', user_id=register_user['user_id'])
    res = auth_client.get(url)
    assert res.status_code == 200

    this_year = str(datetime.now().year)
    this_month = str(datetime.now().month)
    assert this_year and this_month in res.data.decode('utf-8')
