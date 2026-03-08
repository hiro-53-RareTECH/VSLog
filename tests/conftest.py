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
    app = create_app(UnitTestingConfig, load_env=False)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def common_test_password():
    common_test_password = 'register1234'
    return common_test_password

@pytest.fixture()
def register_user_id(app, common_test_password):
    with app.app_context():
        user = User(
            user_id=uuid.uuid4(),
            username='register_user',
            email='register@gmail.com',
            password=hash_password(common_test_password),
        )
        db.session.add(user)
        db.session.commit()

        return user.user_id

@pytest.fixture()
def existing_user(app, common_test_password):
    with app.app_context():
        user = User(
            user_id=uuid.uuid4(),
            username='testuser',
            email='testemail@gmail.com',
            password=hash_password(common_test_password),
        )
        db.session.add(user)
        db.session.flush()

        return user

@pytest.fixture()
def login_user(app, client, register_user_id, common_test_password):
    with app.test_request_context():
        login_user = db.session.get(User, register_user_id)
        form_data = {'email': login_user.email, 'password': common_test_password}
        res = client.post(url_for('auth.login_process'), data=form_data, follow_redirects=True)
        return login_user
