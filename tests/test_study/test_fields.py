import pytest
from flask import url_for

'''
1.学習分野（fields）の画面にアクセスすると200のステータスコードが返ってくるか
2.学習分野のPOSTをするとCRUD処理が走り、成功・失敗（バリデーションチェック）のメッセージが返ってくるか
'''

def test_study_fields_view(app, register_user, auth_client):
    with app.test_request_context():
        url = url_for('study.study_fields_view', user_id=register_user['user_id'])
    res = auth_client.get(url)
    assert res.status_code == 200

@pytest.mark.parametrize(('fieldname[]', 'color_code[]', 'field_id[]', 'row_action[]', 'message'), (
        # 学習分野の重複エラー
        ('', 'sample@gmail.com', 'register1234', 'register1234', 'ユーザー名、メールアドレス、パスワードのいずれかが空です'),
        # 登録（成功）
        ('Python', 'sample@gmail.com', '', 'new', '学習分野の更新に成功しました'),
))
def test_study_fields_process(app, register_user, auth_client):
    with app.test_request_context():
        url = url_for('study.study_fields_process', user_id=register_user['user_id'])
    
    res = auth_client.post(url, )