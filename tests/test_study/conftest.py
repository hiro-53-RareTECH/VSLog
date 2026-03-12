import pytest
from flask import url_for

'''
1.学習分野(fields)のfixture
2.学習記録(logs)のfixture
'''

@pytest.fixture()
def register_fields(app, auth_client, register_user):
    with app.test_request_context():
        url = url_for('study.study_fields_process', user_id=register_user['user_id'])
    form_data = {}
    res = auth_client.post(url, data=form_data, follow_redirects=True)
    

@pytest.fixture()
def register_logs(app, auth_client, register_user, register_fields):
    with app.test_request_context():
        url = url_for('study.study_logs_process', user_id=register_user['user_id'])
    form_data = {}
    res = auth_client.post(url, data=form_data, follow_redirects=True)
