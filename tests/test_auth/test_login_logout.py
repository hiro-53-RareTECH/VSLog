import pytest
from flask import url_for
from src.models.users import User
from src.extensions import db

'''
テスト用ユーザーでログイン、ログアウトができるかの確認テスト
'''

def test_login_form(client, app, register_user_id, common_test_password):
    with app.test_request_context():
        user = db.session.get(User, register_user_id)
        form_data = {'email': user.email, 'password': common_test_password}
        res = client.post(url_for('auth.login_process'), data=form_data, follow_redirects=True)
        assert res.status_code == 200
        assert 'ログインしました' in res.data.decode('utf-8')

def test_logout(client, app):
    with app.test_request_context():
        res = client.get(url_for('auth.logout'))
        assert res.status_code == 302
