def refactor_name(name, code, brand):
    if ('Ballu' in name):
        name = name.replace('Ballu', 'BALLU')
    if ('Ballu Machine' in name):
        name = name.replace('Ballu Machine', 'BALLU MACHINE')
    name = name.replace(brand, '')
    name = name.replace(code, '')
    return f'{code} {name} {brand}'.replace('  ', ' ')
