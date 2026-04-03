import uuid
from src.extensions import db
from src.models.users import User
from src.usecases.adapters import hash_password

def test_db_can_insert_user(app):
    '''
    DBにUserをINSERTできて、再取得できることを確認する最小スモークテスト。
    '''
    with app.app_context():
        u = User(
            user_id=str(uuid.uuid4()),
            username='test_user',
            email='test@gmail.com',
            password=hash_password('password'),
        )

        db.session.add(u)
        db.session.commit()

        found = User.query.filter_by(email='test@gmail.com').first()
        assert found is not None