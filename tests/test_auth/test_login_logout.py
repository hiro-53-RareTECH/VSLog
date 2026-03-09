import pytest
from flask import url_for
from src.models.users import User
from src.extensions import db

'''
テスト用ユーザーでログイン、ログアウトができるかの確認テスト
'''

def test_login_form(client, app, register_user, common_credentials):
    form_data = {'email': register_user['email'], 'password': common_credentials['password']}
    with app.test_request_context():
        res = client.post(url_for('auth.login_process'), data=form_data, follow_redirects=True)
        assert res.status_code == 200
        assert 'ログインしました' in res.data.decode('utf-8')

def test_logout(client, app):
    with app.test_request_context():
        res = client.get(url_for('auth.logout'), follow_redirects=True)
        assert res.status_code == 200
        assert 'ログアウトしました' in res.data.decode('utf-8')
