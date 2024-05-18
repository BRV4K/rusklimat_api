def read_names():
    names = []
    f = open('names.txt')
    for name in f.readlines():
        names.append(name.replace('\n', ''))
    return names



