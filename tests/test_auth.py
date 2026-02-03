import uuid

def test_protected_requires_login(client):
    '''
    未ログイン状態で保護されたページにアクセスしたとき、
    ログイン画面へリダイレクト（302）されるか、あるいは拒否（401）されることを確認。
    '''
    # ログイン必須のURL
    user_id = uuid.uuid4()

    protected_url = f'/dashboard/{user_id}'

    res = client.get(protected_url, follow_redirects=False)

    assert res.status_code in (302, 401)

    if res.status_code == 302:
        location = res.headers.get('Location', '')
        assert '/login' in location or 'login' in location
