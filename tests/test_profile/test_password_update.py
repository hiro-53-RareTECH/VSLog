import pytest
from flask import url_for, request, session
from src.models.users import User
from src.extensions import db

'''
1.パスワード更新画面にGET（200）できるか
2.パスワード更新のためのPOSTを行い、リダイレクトされて、成功（result.ok）の場合、正常なメッセージが返ってくるか。また、失敗の場合（!result.ok）の場合、エラーメッセージが返ってくるか。
'''

def test_password_update_view(client, app, register_user_id):
    with app.test_request_context():
        user = db.session.get(User, register_user_id)
        form_data = {'email': user.email, 'password': 'register1234'}
        res = client.post(url_for('auth.login_process'), data=form_data, follow_redirects=True)
        assert res.status_code == 200
        print(f'debug:{res.data.decode('utf-8')}')
        # assert 'ログインしました' in res.data.decode('utf-8')
        res = client.get(url_for('profile.password_update_view', user_id=register_user_id))
        assert res.status_code == 200

