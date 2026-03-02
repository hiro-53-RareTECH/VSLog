import pytest
from flask import url_for
'''
テスト用ユーザーでログイン、ログアウトができるかの確認テスト
'''

def test_login_form(client):
    form_data = {'email': 'test@gmail.com', 'password': 'password'}
    res = client.post('/login', data=form_data)
    assert res.status_code == 302

def test_logout(client):
    res = client.get('/logout')
    assert res.status_code == 302
