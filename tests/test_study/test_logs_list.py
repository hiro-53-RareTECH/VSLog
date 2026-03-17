import pytest
from flask import url_for
from datetime import datetime, date

'''
1.学習履歴一覧画面（logs_list）にアクセスすると200のステータスコードが返ってくるか
2.学習履歴一覧に年月のJSONを送るとselected_date, study_dictsが返ってくるか
'''

def test_study_logs_list_view(app, auth_client, register_user):
    with app.test_request_context():
        url = url_for('study.study_logs_list_view', user_id=register_user['user_id'])
    res = auth_client.get(url)
    assert res.status_code == 200

    this_year = datetime.now().year
    this_month = datetime.now().month
    this_month_year = date(this_year, this_month, 1).strftime('%Y-%m')
    assert str(this_year) and str(this_month) and this_month_year in res.data.decode('utf-8')

def test_study_logs_list_process(app, auth_client, register_user, register_logs):
    with app.test_request_context():
        url = url_for('study.study_logs_list_process', user_id=register_user['user_id'])
    form_json = {'study_date': '2026-03'}
    res = auth_client.post(url, json=form_json, follow_redirects=True)
    assert res.status_code == 200
    assert res.json['selectedDate'] == '2026-03'
    assert res.json['studyDicts'] == {
        "2026-03-15": [
        {
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
        }
    ]
    }