import uuid
import pytest
from flask import url_for

'''
未ログイン状態で保護されたページにアクセスしたとき、
ログイン画面へリダイレクト（302）されるか、あるいは拒否（401）されることを確認。
'''

@pytest.fixture
def user_id():
    return uuid.uuid4()

@pytest.mark.parametrize('endpoint', [
    'profile.profile_edit_view',
    'profile.password_update_view',
    'study.dashboard_view',
    'study.study_fields_view',
    'study.study_logs_list_view',
    'study.study_logs_view',
])
def test_protected_get_requires_login(client, app, user_id, endpoint):
    with app.test_request_context():
        path = url_for(endpoint.strip(), user_id=user_id)

    res = client.get(path, follow_redirects=False)
    assert res.status_code in (302, 401)

    if res.status_code == 302:
        location = res.headers.get('Location', '')
        assert 'login' in location
