import pytest
from flask import url_for
from datetime import date

'''
1.学習登録画面（logs）にアクセスすると200のステータスコードが返ってくるか
2.
'''

def test_study_logs_view(app, auth_client, register_user):
    with app.test_request_context():
        url = url_for('study.study_logs_view', user_id=register_user['user_id'])
    res = auth_client.get(url)
    assert res.status_code == 200

    today = date.today().strftime('%Y-%m-%d')
    assert today in res.data.decode('utf-8')
