import requests


def get_products(page, token, request_key):
    headers_auth = {"Authorization": token}
    # Получение товаров
    data_products = {"sort": {"brand": "asc"}}
    products_api = requests.post(
        f'https://internet-partner.rusklimat.com/api/v1/InternetPartner/0bf52367-27db-11eb-80d1-48df373819dc/products/{request_key}?pageSize=1000&page={page}',
        headers=headers_auth, json=data_products).json()['data']
    return products_api


def get_token():
    data_auth = {"login": "9221523329", "password": "tWPA1KGJ"}
    token_headers = {"User-Agent": "catalog-ip"}
    # Получение токена
    return requests.post("https://b2b.rusklimat.com/api/v1/auth/jwt/", json=data_auth, headers=token_headers).json()['data']['jwtToken']


def get_request_key(token):
    headers_auth = {"Authorization": token}
    # Получение идентификатора
    return requests.get("https://internet-partner.rusklimat.com/api/v1/InternetPartner/0bf52367-27db-11eb-80d1-48df373819dc/requestKey/", headers=headers_auth).json()['requestKey']


def get_categories(token, request_key):
    headers_auth = {"Authorization": token}
    #Получение категорий
    return requests.get(f'https://internet-partner.rusklimat.com/api/v1/InternetPartner/categories/{request_key}', headers=headers_auth).json()['data']


def get_features(token, request_key):
    headers_auth = {"Authorization": token}
    #Получение свойств
    return requests.get(f'https://internet-partner.rusklimat.com/api/v1/InternetPartner/properties/{request_key}', headers=headers_auth).json()['data']


token = get_token()
rk = get_request_key(token)
