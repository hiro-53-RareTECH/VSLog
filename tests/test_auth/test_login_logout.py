import pytest
from flask import url_for

'''
テスト用ユーザーでログイン、ログアウトができるかの確認テスト
'''

def test_login_form(client, app):
    with app.test_request_context():
        form_data = {'email': 'test@gmail.com', 'password': 'password'}
        res = client.post(url_for('auth.login_process'), data=form_data)
        assert res.status_code == 302

def test_logout(client, app):
    with app.test_request_context():
        res = client.get(url_for('auth.logout'))
        assert res.status_code == 302

