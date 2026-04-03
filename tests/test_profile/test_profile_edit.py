import pytest
import uuid
from flask import url_for
from src.models.users import User
from src.extensions import db
from src.usecases.adapters import hash_password

'''
1.プロフィール更新画面にGET（200）できるか
2.プロフィール更新のためのPOSTを行い、リダイレクトされて、成功（result.ok）の場合、正常なメッセージが返ってくるか。また、失敗の場合（!result.ok）の場合、エラーメッセージが返ってくるか。
'''

def test_profile_edit_view(app, auth_client, register_user):
    with app.test_request_context():
        url = url_for('profile.profile_edit_view', user_id=register_user['user_id'])
    res = auth_client.get(url)
    assert res.status_code == 200

@pytest.mark.parametrize(('new_username', 'new_email', 'message'), (
        # いずれかが空白
        ('new_testuser', '', '空のフォームがあります'),
        # メールアドレスの形式不整合
        ('new_testuser', 'new_email', 'メールアドレスの形式になっていません'),
        # 既に登録されているメールアドレス
        ('new_testuser', 'another_register', '既に登録されているメールアドレスです'),
        # 成功（ユーザー名のみ変更）
        ('new_testuser', 'register', 'プロフィール編集が完了しました'),
        # 成功（ユーザー名、emailどちらも変更）
        ('new_testuser', 'new_email@gmail.com', 'プロフィール編集が完了しました'),
))
def test_profile_edit_process(app, auth_client, register_user, another_register_user, new_username, new_email, message):
    with app.test_request_context():
        url = url_for('profile.profile_edit_process', user_id=register_user['user_id'])
    if new_email == 'register':
        new_email = register_user['email']
    if new_email == 'another_register':
        new_email = another_register_user['email']
    form_data = {'new_username': new_username, 'new_email': new_email}
    res = auth_client.post(url, data=form_data, follow_redirects=True)
    assert res.status_code == 200
    assert message in res.data.decode('utf-8')
