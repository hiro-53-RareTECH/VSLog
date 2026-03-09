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

@pytest.mark.parametrize(('current_password', 'new_password1', 'new_password2', 'message'), (
        # いずれかが空白
        ('register', '', 'update_password', '空のフォームがあります'),
        # 現在のパスワードが正しくない
        ('diff_password', 'update_password', 'update_password', '現在のパスワードが正しくありません'),
        # 異なるパスワード
        ('register', 'update_password', 'password_update', '新しいパスワードと新しいパスワード（確認用）が一致しません'),
        # パスワードの文字列8文字以上16文字以内
        ('register', 'test', 'test', 'パスワードは8文字以上16文字以内で入力してください'),
        # 成功
        ('register', 'update_password', 'update_password', 'パスワード変更が完了しました'),
))
def test_password_update_process(app, auth_client, register_user, common_credentials, current_password, new_password1, new_password2, message):
    with app.test_request_context():
        url = url_for('profile.password_update_process', user_id=register_user['user_id'])
    if current_password == 'register':
        current_password = common_credentials['password']
    form_data = {'current_password': current_password, 'new_password1': new_password1, 'new_password2': new_password2}
    res = auth_client.post(url, data=form_data, follow_redirects=True)
    assert res.status_code == 200
    assert message in res.data.decode('utf-8')
