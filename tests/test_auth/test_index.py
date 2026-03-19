import pytest
from flask import url_for
from src.models.users import User
from src.extensions import db

'''
1.index画面にアクセスすると200のステータスコードが返ってくるか
'''

def test_index_view(app, client):
    with app.test_request_context():
        url = url_for('auth.index_view')
    res = client.get(url)
    assert res.status_code == 200
