from get_data import *


def refactor_props(props):
    ref_props = {}
    for prop in props:
        id_prop = prop['id']
        if 'priceRrc' in id_prop:
            continue
        name_prop = prop['name']
        if 'Интернет наименование_товара' in name_prop:
            continue
        if 'html описания_товара' in name_prop:
            continue
        if 'Маркер карточки' in name_prop:
            continue
        if 'пиктограмма' in name_prop:
            continue
        if 'Бренд' in name_prop:
            continue
        if 'Большое изображение' in name_prop:
            continue
        if 'Эксклюзив' in name_prop:
            continue

        ref_props[id_prop] = name_prop
    return ref_props
