from get_data import *
from refactor_cats import refactor_categories
from get_full_category import get_full_category
import csv
import os

brands_to_do = ['Royal Thermo', 'BALLU', 'Electrolux', 'BALLU MACHINE', 'SHUFT']
brands = []

token = get_token()
request_key = get_request_key(token)
categories_api = get_categories(token, request_key)
categories = refactor_categories(categories_api)
feauters = get_features(token, request_key)

for i in range(1, 20):
    products = get_products(i, token, request_key)
    for product in products:
        brand = product['brand']
        if brand not in brands_to_do:
            continue
        code = product['nsCode']
        category_id = product['categoryId']
        full_category = get_full_category(category_id, categories)
        full_category.reverse()
        full_category = '/'.join(full_category)
        articul = product['vendorCode']
        name = product['name']
        props = product['properties']
        pictures = product['pictures']
        description = product['description']
        price_rrc = product['price']
        price_ric = product['internetPrice']
        price_client = product['clientPrice']
        ostatok_total = product['remains']['total']
        ostatok_detail = product['remains']['warehouses']

        row = {'name': name, 'brand': brand, 'category': full_category,'code': code, 'articul': articul, 'price_rrc': price_rrc,
               'price_ric': price_ric, 'price_client': price_client, 'ostatok_total': ostatok_total,
               'ostatok_detail': ostatok_detail}

        first_row = {'name': 'Наименование', 'brand': "Бренд", 'category': 'Категория', 'code': "Код товара", 'articul': "Артикул",
                     'price_rrc': "Цена РРЦ", 'price_ric': "Цена РИЦ", 'price_client': "Цена для клиентов",
                     'ostatok_total': "Суммарный остаток", 'ostatok_detail': "Остаток по складам"}

        with open(f'files_brands/{brand}.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'brand', 'category', 'code', 'articul', 'price_rrc',
                                                      'price_ric', 'price_client', 'ostatok_total', 'ostatok_detail'])
            if os.stat(f'files_brands/{brand}.csv').st_size == 0:
                writer.writerow(first_row)
            writer.writerow(row)

