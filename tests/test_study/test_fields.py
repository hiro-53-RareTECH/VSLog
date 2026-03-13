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
        ('Docker', '#000000', '', 'new', f'{fieldname}は既に登録されています'),
        # 登録（成功）
        ('Python', '#000000', '', 'new', '学習分野の更新に成功しました'),
        # 編集（成功）
        ('Python', '#000000', '', 'update', '学習分野の更新に成功しました'),
        # 削除（成功）
        ('Python', '#000000', '', 'delete', '学習分野の更新に成功しました'),

))
def test_study_fields_process(app, register_user, auth_client):
    with app.test_request_context():
        url = url_for('study.study_fields_process', user_id=register_user['user_id'])
    
    res = auth_client.post(url, )