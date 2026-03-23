import pytest
from flask import url_for, abort
from unittest.mock import patch

'''
1.存在しないURLにアクセスして、ステータスコード404が返ってくるか確認し、確認後に指定したHTMLコンテンツが含まれているかどうか
2.認証前に権限の必要なページ（study, profile）にアクセスし、403が返ってくるか確認し、確認後に指定したHTMLコンテンツが含まれているかどうか
3.500エラーを強制的に発生させ、500が返ってくるか確認し、確認後に指定したHTMLコンテンツが含まれているかどうか
'''

def test_page_not_found(app, client):
    res = client.get('/test-page-not-found')
    assert res.status_code == 404
    assert '<h1>404<br/>Page Not Found</h1>' in res.data.decode('utf-8')

@pytest.mark.parametrize('url', ['study.dashboard_view', 'study.study_fields_view', 'study.study_logs_list_view', 'study.study_logs_view', 'profile.password_update_view', 'profile.profile_edit_view'])
def test_forbidden_error(app, auth_client, url):
    with app.test_request_context():
        dummy_user_id = 123456789
        form_url = url_for(url, user_id=dummy_user_id)
    res = auth_client.get(form_url)
    assert res.status_code == 403
    assert '<h1>403<br />Forbidden</h1>' in res.data.decode('utf-8')

@pytest.mark.parametrize(('url', 'target'), (
                         ('study.get_graph_stats', 'src.usecases.study.get_graph_stats.get_graph_stats_usecase'),
                        )
                        )
def test_internal_server_error(app, auth_client, register_user, url, target):
    with patch(target, side_effect=Exception('Internal Server Error')):
        res = auth_client.post(url_for(url, user_id=register_user['user_id']) )
        assert res.status_code == 500
        assert '<h1>500<br />Internal Server Error</h1>' in res.data.decode('utf-8')
