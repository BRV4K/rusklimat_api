import requests
import json

#Ручной токен
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTMyMjU2MDAsImd1aWQiOiIwYmY1MjM2Ny0yN2RiLTExZWItODBkMS00OGRmMzczODE5ZGMiLCJndWlkUk0iOm51bGwsImd1aWRMZWFkIjpudWxsLCJndWlkTWFuYWdlciI6bnVsbH0.o62GOmz-c59bDphXa0hCwEQRt9Mg7Nk2NNGn16JGDDY'

# data_auth = {'login": '9221523329', "password": 'tWPA1KGJ'}
payload = {'login': '9221523329', 'password': 'tWPA1KGJ'}
headers = {'User-agent': 'catalog-ip'}

# payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://b2b.rusklimat.com/api/v1/auth/jwt/", headers=headers, json=payload)
print(r.text)

token_auto = r.json()['data']['jwtToken']
print(token_auto)


# headers = {'Authorization': token}

#Получение идентификатора
# r=requests.get("https://internet-partner.rusklimat.com/api/v1/InternetPartner/0bf52367-27db-11eb-80d1-48df373819dc/requestKey/", headers={"CAuthorization": token_auto})
# print(r.text)

#Получение категорий товаров
# caregories = requests.get(f'https://internet-partner.rusklimat.com/api/v1/InternetPartner/categories/63848761555000000').json()
# print('categories: ', caregories)

#Получение товаров
headers = { 'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTMyMjU2MDAsImd1aWQiOiIwYmY1MjM2Ny0yN2RiLTExZWItODBkMS00OGRmMzczODE5ZGMiLCJndWlkUk0iOm51bGwsImd1aWRMZWFkIjpudWxsLCJndWlkTWFuYWdlciI6bnVsbH0.o62GOmz-c59bDphXa0hCwEQRt9Mg7Nk2NNGn16JGDDY'}

payload = {'columns': ['name','nsCode','price','clientPrice', 'brand'],'filter': {'categoryIds': ['f7a25385-f2ad-411b-9410-bd9c6fa386ce','194602b6-2e40-4b6e-996c-89774e5b9fc1', 'd2257a3e-4298-4e9b-8db7-5b6bfe62c76d']},'sort': {'nsCode': 'asc'} }

data = requests.post('https://internet-partner.rusklimat.com/api/v1/InternetPartner/0bf52367-27db-11eb-80d1-48df373819dc/products/63848759751000000/?pageSize=500&page=1',
                     headers=headers, json=payload)
print(data.text)
