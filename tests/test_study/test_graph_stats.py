import pytest
from flask import url_for

'''
1.グラフ描画、統計値取得の処理にJSONデータを送り、svg、total_day、total_hour、avg_hourがレスポンスできるか
2.fieldsとlineが選択された時（本来は選択できないが）にValueErrorが出るか
'''

period = ['this_week', 'last_week', 'month', 'year', 'all']
year = '2026'
monthYear = '2026'
month = '3'
horizontalAxis = ['days', 'fields']
verticalAxis = ['time', 'percent']
graphType = ['bar', 'pie', 'line']

testdata = []
test_error_data = []
for p in period:
    for h in horizontalAxis:
        for v in verticalAxis:
            for g in graphType:
                input_data = [p, year, monthYear, month, h, v, g]
                if h == 'fields' and g == 'line':
                    test_error_data.append(input_data)
                else:
                    testdata.append(input_data)

@pytest.mark.parametrize('period, year, monthYear, month, horizontalAxis, verticalAxis, graphType', testdata)
def test_get_graph_stats(app, auth_client, register_user, register_logs, period, year, monthYear, month, horizontalAxis, verticalAxis, graphType):
    with app.test_request_context():
        url = url_for('study.get_graph_stats', user_id=register_user['user_id'])
    form_json = {'period': period, 'year': year, 'month-year': monthYear, 'month': month, 'horizontalAxis': horizontalAxis, 'verticalAxis': verticalAxis, 'graphType': graphType}
    res = auth_client.post(url, json=form_json, follow_redirects=True)
    assert res.status_code == 200
    assert isinstance(res.json['svg'], str) or res.json['svg'] == None
    assert isinstance(res.json['total_day'], int)
    assert isinstance(res.json['total_hour'], float)
    assert isinstance(res.json['avg_hour'], float)

@pytest.mark.parametrize('period, year, monthYear, month, horizontalAxis, verticalAxis, graphType', test_error_data)
def test_error_get_graph_stats(app, auth_client, register_user, register_logs, period, year, monthYear, month, horizontalAxis, verticalAxis, graphType):
    with app.test_request_context():
        url = url_for('study.get_graph_stats', user_id=register_user['user_id'])
    with pytest.raises(ValueError) as e:
        form_json = {'period': period, 'year': year, 'month-year': monthYear, 'month': month, 'horizontalAxis': horizontalAxis, 'verticalAxis': verticalAxis, 'graphType': graphType}
        res = auth_client.post(url, json=form_json, follow_redirects=True)
        raise ValueError(f'invalid graphType: {graphType}')
    assert e.type is ValueError
    assert e.value.args[0] == f'invalid graphType: {graphType}'
