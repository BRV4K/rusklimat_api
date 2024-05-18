from get_data import *
from refactor_cats import refactor_categories

categories = refactor_categories(get_categories(get_token(), get_request_key(get_token())))


def get_full_category(id, categories):
    ful_cat = [categories[id]['name']]
    while True:
        parent_id = categories[id]['parent']
        if parent_id == None:
            return ful_cat
        else:
            ful_cat.append(categories[parent_id]['name'])
            id = parent_id
