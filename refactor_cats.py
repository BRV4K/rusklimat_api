def refactor_categories(categories):
    ref_cats = {}
    for category in categories:
        cat_id = category['id']
        cat_name = category['name']
        cat_parent = category['parent']
        ref_cats[cat_id] = {'name': cat_name, 'parent': cat_parent}
    return ref_cats
