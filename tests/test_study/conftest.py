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
    form_data = {'fieldname[]': ['Docker', 'Git', 'Linux', 'Java'], 'color_code[]': ['#000000', '#555555', '#888888', '#891413'], 'field_id[]': ['', '', '', ''], 'row_action[]': ['new', 'new', 'new', 'new']}
    res = auth_client.post(url, data=form_data, follow_redirects=True)
    assert res.status_code == 200
    assert '学習分野の更新に成功しました' in res.data.decode('utf-8')

@pytest.fixture()
def register_logs(app, auth_client, register_user, register_fields):
    with app.test_request_context():
        url = url_for('study.study_logs_process', user_id=register_user['user_id'])
    form_data = {'study_dates[]': ['2026-03-15', '2026-03-15', '2026-03-15'], 'hours[]': [1, 2, 3], 'fieldnames[]': ['Docker', 'Git', 'Linux'], 'contents[]': ['aaa', 'bbb', 'ccc'], 'study_log_ids[]': ['', '', ''], 'row_actions[]': ['new', 'new', 'new']}
    res = auth_client.post(url, data=form_data, follow_redirects=True)
    assert res.status_code == 200
    assert '学習記録の更新が完了しました' in res.data.decode('utf-8')
