import pytest
from flask import url_for, request, session
from src.models.users import User

'''
パスワード変更のフォームが送信されて、ログイン画面にリダイレクトされるか
パスワード変更時のバリデーションが正常に動作するか
'''

def test_password_reset_process(client, app, existing_user):
    with app.test_request_context():
        form_data = {'email': existing_user.email, 'new_password1': 'new_test1234', 'new_password2': 'new_test1234'}
        res = client.post(url_for('auth.password_reset_process'), data=form_data)
        assert res.status_code == 302

@pytest.mark.parametrize(('email', 'new_password1', 'new_password2', 'message'),(
        # 空のフォーム
        ('existing', 'new_test1234', '', '空のフォームがあります'),
        # パスワード不一致
        ('existing', 'new_test1234', 'new_test4321', 'パスワードが一致しません'),
        # パスワード文字数
        ('existing', 'test', 'test', 'パスワードは8文字以上16文字以内で入力してください'),
        # 登録されていないemail
        ('test_reset@gmail.com', 'new_test1234', 'new_test1234', '登録されていないメールアドレスです'),
))
def test_password_reset_validation(client, app, email, new_password1, new_password2, message, existing_user):
    with app.test_request_context():
        if email == 'existing':
            email = existing_user.email
        form_data = {'email': email, 'new_password1': new_password1, 'new_password2': new_password2}
        res = client.post(url_for('auth.password_reset_process'), data=form_data, follow_redirects=True)

        assert res.status_code == 200
        assert message in res.data.decode('utf-8')
