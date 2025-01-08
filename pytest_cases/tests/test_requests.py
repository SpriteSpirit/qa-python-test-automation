import requests

from utilities.logger_utils import logger

base_url = "http://5.101.50.27:8000"


def test_simple_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')
    response_body = resp.json()
    first_company = response_body[0]
    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"


def test_auth():
    user_creds = {
        "username": "harrypotter",
        "password": "expelliarmus"
    }

    # company = {
    #     "name": "QA Студия 'Тестировщик'",
    #     "description": "Лучшая компания в QA",
    #     "user": user_creds["username"]
    # }

    # авторизация
    resp = requests.post(base_url + '/auth/login', json=user_creds)
    token = resp.json()['user_token']
    logger.debug(token)
    assert resp.status_code == 200

    # # создание компании с авторизацией
    # headers = {"x-client-token": token}
    # resp = requests.post(base_url + '/company', json=company, headers=headers)
    # assert resp.status_code == 201
    # created_company = resp.json()
    # assert created_company["name"] == company["name"]
    # assert created_company["description"] == company["description"]
