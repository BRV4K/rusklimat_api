from get_data import *
from refactor_cats import refactor_categories
from refactor_props import refactor_props


def get_max_fields(token, request_key):
    brands_to_do = ['Royal Thermo', 'BALLU', 'Electrolux', 'BALLU MACHINE', 'SHUFT']
    categories_api = get_categories(token, request_key)
    categories = refactor_categories(categories_api)
    feauters_api = get_features(token, request_key)
    properties = refactor_props(feauters_api)  # {id: name}

    max_fields = {}
    for i in range(1, 20):
        products = get_products(i, token, request_key)
        for product in products:
            brand = product['brand']
            if brand not in brands_to_do:
                continue
            category_name = categories[product['categoryId']]['name']
            props = product['properties']
            images_len = len(product['pictures'])
            if category_name not in max_fields:
                max_fields[category_name] = props
                max_fields[category_name]['images'] = images_len
            else:
                for prop in props:
                    if prop not in max_fields[category_name] and prop in properties:
                        max_fields[category_name][prop] = props[prop]
                if images_len > max_fields[category_name]['images']:
                    max_fields[category_name]['images'] = images_len
    return max_fields


token = get_token()
rk = get_request_key(token)
