import pytest
from flask import url_for, request, session
from src.models.users import User
from src.extensions import db

'''
新規登録後にダッシュボードのURLへリダレクト（302）されるかどうか
新規登録時のバリデーションが正常に行われるか
'''

def test_signup_form(client, app, common_test_password):
    with app.test_request_context():
        form_data = {'username': 'testuser', 'email': 'testemail@gmail.com', 'password1': common_test_password, 'password2': common_test_password}
        res = client.post(url_for('auth.signup_process'), data=form_data)
        assert res.status_code == 302

        user = User.query.filter_by(email=form_data['email']).first()
        user_id = user.user_id
        assert res.headers['Location'] == url_for('study.dashboard_view', user_id=user_id)

@pytest.mark.parametrize(('username', 'email', 'password1', 'password2', 'message'), (
        # username空白
        ('', 'sample@gmail.com', 'register1234', 'register1234', 'ユーザー名、メールアドレス、パスワードのいずれかが空です'),
        # 既に登録されているemail
        ('testuser', 'register', 'register1234', 'register1234', '既に登録されているメールアドレスです'),
        # 異なるパスワード
        ('testuser', 'sample@gmail.com', 'register1234', 'register4321', 'パスワードが一致しません'),
        # パスワードの文字列8文字以上16文字以内
        ('testuser', 'sample@gmail.com', 'test', 'test', 'パスワードは8文字以上16文字以内で入力してください'),
))
def test_signup_validate(client, app, username, email, password1, password2, message, register_user_id):
    with app.test_request_context():
        if email == 'register':
            user = db.session.get(User, register_user_id)
            email = user.email
        res = client.post(url_for('auth.signup_process'), data={
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2,
            }, follow_redirects=True)
        
        assert res.status_code == 200
        assert message in res.data.decode('utf-8')
