from get_data import *
from refactor_cats import refactor_categories
from get_full_category import get_full_category
from find_max_fields import get_max_fields
from create_description import create_description
from refactor_name import refactor_name
from create_url import create_url
from refactor_props import refactor_props
from names_to_do import read_names
from clean_files import clean_files

from claim_categories import claim_right_cats
from claim_images import claim_right_images

import csv
import os

brands_to_do = ['Royal Thermo', 'BALLU', 'Electrolux', 'BALLU MACHINE', 'SHUFT']
brands = []

token = get_token()
request_key = get_request_key(token)
categories_api = get_categories(token, request_key)
categories = refactor_categories(categories_api) # {id: name, parent}
feauters_api = get_features(token, request_key)
properties = refactor_props(feauters_api) # {id: name}
names_to_do = read_names()

right_images = claim_right_images()
right_cats = claim_right_cats()

max_fields = get_max_fields(token, request_key)

for i in range(1, 20):
    print(i)
    products = get_products(i, token, request_key)
    for product in products:
        brand = product['brand']
        if brand not in brands_to_do:
            continue
        code = product['vendorCode']
        if code not in names_to_do:
            continue
        url = create_url(code)
        category_id = product['categoryId']
        full_category = get_full_category(category_id, categories)
        full_category.reverse()
        if full_category[-1] not in right_cats:
            continue
        right_category = right_cats[full_category[-1]]
        articul = product['vendorCode']
        name = product['name']
        name = refactor_name(name, code, brand)
        if name not in right_images:
            continue
        props = product['properties']
        description = product['description']
        description = create_description(name, description)
        price_rrc = product['price']
        price_ric = product['internetPrice']
        if price_ric == '' or price_ric == None:
            continue
        price_client = product['clientPrice']
        ostatok_total = product['remains']['total']
        ostatok_detail = product['remains']['warehouses']

        sklads = []
        if len(ostatok_detail) != 0:
            for sklad in ostatok_detail:
                if 'екатеринбург' in sklad.lower():
                    sklads.append('Екатеринбург')
                if 'киржач' in sklad.lower():
                    sklads.append('Киржач')
                if 'лакинск' in sklad.lower():
                    sklads.append('Лакинск')
                if 'орехово-зуево' in sklad.lower():
                    sklads.append('Орехово-Зуево')
                if 'петушки' in sklad.lower():
                    sklads.append('Петушки')

        bf1 = ["Наименование", "Артикул", "Валюта", "Цена, с НДС", "В наличии", "Доступен для заказа",
               "Краткая информация", "Описание", "Наклейка", "Статус", "Теги", "Meta Title",
               "Meta Description", "URL", "Срок изготовления", "Доставка", "Производитель",
               "Серия", "Код товара"]
        bf2 = []

        pictures = right_images[name]
        if len(pictures) == 0:
            continue
        pictures_dict = {}
        for pict_number in range (len(pictures)):
            bf2.append('Изображения' + str(pict_number))
            pictures_dict['Изображения' + str(pict_number)] = pictures[pict_number]

        max_fields_cur = max_fields[full_category[-1]]

        field_names = []
        for fild in max_fields_cur:
            if fild not in properties:
                continue
            field_names.append(properties[fild])
        field_names = bf1 + field_names + bf2

        cur_props = {}
        for key, value in props.items():
            prop_name_id = key
            if prop_name_id not in properties:
                continue
            prop_value = value
            if prop_value.count('-') >= 3:
                continue
            prop_name = properties[prop_name_id]
            if prop_name == 'Артикул':
                series = prop_value
                continue
            if prop_name == 'Серия':
                series = prop_value
                continue
            cur_props[prop_name] = prop_value

        row = {"Наименование": name,
               "Валюта": 'RUB',
               "Цена, с НДС": price_ric,
               "В наличии": 0 if (ostatok_total.lower() == 'ожидается поставка' or ostatok_total.lower() == 'под заказ') else 1,
               "Доступен для заказа": 1,
               "Описание": description,
               "Статус": 1,
               "Meta Title": f'Купить {name} с доставкой на uralenergotel.ru',
               "Meta Description": f'Купить {name} по низкой цене у официального дилера ТД УЭТ',
               "URL": url,
               "Срок изготовления": 'Уточняйте у менеджера',
               "Доставка": 'Доставка со складов: Екатеринбург, Киржач, Орехово-Зеуво, Лакинск, Петушки',
               "Производитель": brand,
               "Серия": series,
               "Код товара": code}
        for pict in pictures_dict:
            row[pict] = pictures_dict[pict]

        row = dict(list(row.items()) + list(cur_props.items()))

        first_row = {}
        for field in field_names:
            if 'Изображения' in field:
                first_row[field] = 'Изображения'
            else:
                first_row[field] = field

        with open(f'files/{brand}/{full_category[-1]}.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            if os.stat(f'files/{brand}/{full_category[-1]}.csv').st_size == 0:
                writer.writerow(first_row)
                for j in range(len(right_category)):
                    writer.writerow({'Наименование': right_category[j]})
            writer.writerow(row)

clean_files()
