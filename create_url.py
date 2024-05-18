def create_url(code):
    url = code.lower()
    url = url.replace(' ', '_')
    url = url.replace('-', '_')
    url = url.replace('/', '_')
    url = url.replace('\\', '_')
    url = url.replace('.', '_')
    url = url.replace(',', '_')
    url = url.replace(';', '_')
    url = url.replace(':', '_')
    url = url.replace('+', 'plus')
    return url
