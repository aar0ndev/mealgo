import pytest
import requests

TEST_URL = 'http://localhost:5000'
_token = None


@pytest.fixture
def token():
    global _token
    if _token:
        return _token
    ret = requests.post(
        TEST_URL + '/login',
        data='{"email":"user@test.com","password":"password"}',
        headers={'Content-Type': 'application/json'},
    )
    _token = ret.text
    return _token


def test_index():
    ret = requests.get(TEST_URL)
    assert len(ret.json()) == 1


def test_login():
    ret = requests.post(
        TEST_URL + '/login',
        data='{"email":"user@test.com","password":"password"}',
        headers={'Content-Type': 'application/json'},
    )
    print(ret.text)
    assert ret.status_code == 200

    token = ret.text
    assert len(token) > 0


def test_userinfo(token):
    ret = requests.get(TEST_URL + '/userinfo', headers={'Auth-Token': token},)
    print(ret.text)
    assert ret.status_code == 200
    assert ret.json()['user']['email'] == 'user@test.com'


# def test_login():
