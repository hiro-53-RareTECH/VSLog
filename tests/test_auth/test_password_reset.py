import pytest
from flask import url_for
from src.models.users import User

'''
パスワード変更のフォームが送信されて、ログイン画面にリダイレクトされるか
パスワード変更時のバリデーションが正常に動作するか
'''

def test_password_reset_process(client, app, register_user):
    with app.test_request_context():
        form_data = {'email': register_user['email'], 'new_password1': 'new_test1234', 'new_password2': 'new_test1234'}
        res = client.post(url_for('auth.password_reset_process'), data=form_data, follow_redirects=True)
        assert res.status_code == 200
        assert 'パスワード再設定が完了しました' in res.data.decode('utf-8')

@pytest.mark.parametrize(('email', 'new_password1', 'new_password2', 'message'),(
        # 空のフォーム
        ('register', 'new_test1234', '', '空のフォームがあります'),
        # パスワード不一致
        ('register', 'new_test1234', 'new_test4321', 'パスワードが一致しません'),
        # パスワード文字数
        ('register', 'test', 'test', 'パスワードは8文字以上16文字以内で入力してください'),
        # 登録されていないemail
        ('test_reset@gmail.com', 'new_test1234', 'new_test1234', '登録されていないメールアドレスです'),
))
def test_password_reset_validation(client, app, email, new_password1, new_password2, message, register_user):
    with app.test_request_context():
        if email == 'register':
            email = register_user['email']
        form_data = {'email': email, 'new_password1': new_password1, 'new_password2': new_password2}
        res = client.post(url_for('auth.password_reset_process'), data=form_data, follow_redirects=True)

        assert res.status_code == 200
        assert message in res.data.decode('utf-8')
