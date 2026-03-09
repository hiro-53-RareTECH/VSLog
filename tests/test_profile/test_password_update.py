import pytest
from flask import url_for
from src.models.users import User
from src.extensions import db

'''
1.パスワード更新画面にGET（200）できるか
2.パスワード更新のためのPOSTを行い、リダイレクトされて、成功（result.ok）の場合、正常なメッセージが返ってくるか。また、失敗の場合（!result.ok）の場合、エラーメッセージが返ってくるか。
'''

def test_password_update_view(app, auth_client, register_user):
    with app.test_request_context():
        url = url_for('profile.password_update_view', user_id=register_user['user_id'])
    res = auth_client.get(url)
    assert res.status_code == 200

def test_password_update_process(app, auth_client, register_user, common_credentials):
    with app.test_request_context():
        url = url_for('profile.password_update_process', user_id=register_user['user_id'])
    form_data = {'current_password': common_credentials['password'], 'new_password1': 'update_password', 'new_password2': 'update_password'}
    res = auth_client.post(url, data=form_data, follow_redirects=True)
    assert res.status_code == 200
    assert 'パスワード変更が完了しました' in res.data.decode('utf-8')
