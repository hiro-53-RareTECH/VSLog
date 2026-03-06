import pytest
from flask import url_for
from src.models.users import User
from src.extensions import db
from src.usecases.adapters import hash_password


'''
テスト用ユーザーでログイン、ログアウトができるかの確認テスト
'''

def test_login_form(client, app, register_user_id):
    with app.test_request_context():
        user = db.session.get(User, register_user_id)
        form_data = {'email': user.email, 'password': 'register1234'}
        res = client.post(url_for('auth.login_process'), data=form_data, follow_redirects=True)
        print(hash_password('register1234'), user.password)
        print(res.data.decode('utf-8'))
        assert res.status_code == 200
        assert 'ログインしました' in res.data.decode('utf-8')

def test_logout(client, app):
    with app.test_request_context():
        res = client.get(url_for('auth.logout'))
        assert res.status_code == 302

