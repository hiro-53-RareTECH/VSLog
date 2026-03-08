import pytest
from flask import url_for
from src.models.users import User
from src.extensions import db

'''
1.パスワード更新画面にGET（200）できるか
2.パスワード更新のためのPOSTを行い、リダイレクトされて、成功（result.ok）の場合、正常なメッセージが返ってくるか。また、失敗の場合（!result.ok）の場合、エラーメッセージが返ってくるか。
'''

def test_password_update_view(client, app, login_user):
    with app.test_request_context():
        res = client.get(url_for('profile.password_update_view', user_id=login_user.user_id))
        assert res.status_code == 200

def test_password_update_process(client, app, login_user, common_test_password):
    with app.test_request_context():
        form_data = {'current_password': common_test_password, 'new_password1': 'update_password', 'new_password2': 'update_password'}
        res = client.post(url_for('profile.password_update_process', user_id=login_user.user_id), data=form_data, follow_redirects=True)
        assert res.status_code == 200
        print(res.data.decode('utf-8'))
        assert 'パスワード変更が完了しました' in res.data.decode('utf-8')
