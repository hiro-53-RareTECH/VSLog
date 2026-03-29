import pytest
from flask import url_for
from datetime import date

'''
1.学習記録画面（logs）にアクセスすると200のステータスコードが返ってくるか
2.学習記録に日付のJSONを送ると選択した日付の学習記録が返ってくるか
3.学習記録のPOSTをするとCRUD処理が走り、成功・失敗（バリデーションチェック）のメッセージが返ってくるか
'''

def test_study_logs_view(app, auth_client, register_user, register_logs):
    with app.test_request_context():
        url = url_for('study.study_logs_view', user_id=register_user['user_id'])
    res = auth_client.get(url)
    assert res.status_code == 200
    today = date.today().strftime('%Y-%m-%d')
    assert today in res.data.decode('utf-8')

    form_json = {'study_date': '2026-03-15'}
    res = auth_client.post(url, json=form_json, follow_redirects=True)
    assert res.status_code == 200
    assert res.json['selected_date'] == '2026-03-15'
    assert res.json['studyDicts'] == [{
      "content": "aaa",
      "fieldname": "Docker",
      "hour": 1.0,
      "study_date": "2026-03-15",
      "study_log_id": 1
    },
    {
      "content": "bbb",
      "fieldname": "Git",
      "hour": 2.0,
      "study_date": "2026-03-15",
      "study_log_id": 2
    },
    {
      "content": "ccc",
      "fieldname": "Linux",
      "hour": 3.0,
      "study_date": "2026-03-15",
      "study_log_id": 3
    }]

@pytest.mark.parametrize(('study_dates', 'hours', 'fieldnames', 'contents', 'study_log_ids', 'row_actions', 'message'), (
        # 学習分野の未登録エラー
        ('2026-03-15', 1.5, 'Python', 'aaa', '', 'new', 'Pythonが登録されていません。先に学習分野の登録をお願いします。'),
        # 登録（成功）
        ('2026-03-15', 1.5, 'Java', '登録', '', 'new', '学習記録の更新が完了しました'),
        # 編集（成功）
        ('2026-03-15', 1.5, 'Docker', '編集', 1, 'update', '学習記録の更新が完了しました'),
        # 削除（成功）
        ('2026-03-15', 1.5, 'Git', '削除', '2', 'delete', '学習記録の更新が完了しました'),
        # 学習日が選択されていない
        ('', 1.5, 'Java', '登録', '', 'new', '学習日を選択してください'),
))
def test_study_logs_process(app, auth_client, register_user, register_logs, study_dates, hours, fieldnames, contents, study_log_ids, row_actions, message):
    with app.test_request_context():
        url = url_for('study.study_logs_process', user_id=register_user['user_id'])
    form_data = {'study_dates[]': study_dates, 'hours[]': hours, 'fieldnames[]': fieldnames, 'contents[]': contents, 'study_log_ids[]': study_log_ids, 'row_actions[]': row_actions}
    res = auth_client.post(url, data=form_data, follow_redirects=True)
    assert res.status_code == 200
    print(res.data.decode('utf-8'))
    assert message in res.data.decode('utf-8')
