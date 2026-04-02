import pytest
import uuid
from flask import url_for
from src import create_app
from src.config import UnitTestingConfig
from src.models.users import User
from src.extensions import db
from src.usecases.adapters import hash_password

@pytest.fixture()
def app():
    app = create_app(UnitTestingConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def common_credentials():
    common_user_id = uuid.uuid4()
    common_username = 'register_user'
    common_email = 'register@gmail.com'
    common_password = 'register1234'
    return {'user_id': common_user_id,
            'username': common_username,
            'email': common_email,
            'password': common_password,
            }

@pytest.fixture()
def register_user(app, common_credentials):
    with app.app_context():
        user = User(
            user_id=common_credentials['user_id'],
            username=common_credentials['username'],
            email=common_credentials['email'],
            password=hash_password(common_credentials['password']),
        )
        db.session.add(user)
        db.session.commit()

        return {'user_id': user.user_id,
                'username': user.username,
                'email': user.email,
                'password': user.password,
                }

@pytest.fixture()
def another_register_user(app):
    with app.app_context():
        user = User(
            user_id=uuid.uuid4(),
            username='another_register_user',
            email='another_register@gmail.com',
            password=hash_password('another_register'),
        )
        db.session.add(user)
        db.session.commit()

        return {'user_id': user.user_id,
                'username': user.username,
                'email': user.email,
                'password': user.password,
                }

@pytest.fixture()
def auth_client(app, client, register_user, common_credentials):
    with app.test_request_context():
        url = url_for('auth.login_process')
    form_data = {'email': register_user['email'], 'password': common_credentials['password']}
    res = client.post(url, data=form_data, follow_redirects=True)
    assert res.status_code == 200
    return client
