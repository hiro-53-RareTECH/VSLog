import pytest
import uuid
from src import create_app
from src.config import UnitTestingConfig
from src.models.users import User
from src.extensions import db
from src.usecases.adapters import hash_password, verify_password

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
def register_user_id(app):
    with app.app_context():
        user = User(
            user_id=uuid.uuid4(),
            username='register_user',
            email='register@gmail.com',
            password=hash_password('register1234'),
        )
        db.session.add(user)
        db.session.commit()

        print(user.password)
        print(type(user.password))
        print(verify_password(user.password, 'register1234'))

        return user.user_id

@pytest.fixture()
def existing_user(app):
    with app.app_context():
        user = User(
            user_id=uuid.uuid4(),
            username='testuser',
            email='testemail@gmail.com',
            password=hash_password('test1234'),
        )
        db.session.add(user)
        db.session.flush()

        return user
