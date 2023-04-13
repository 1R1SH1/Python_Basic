import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

box = []


def web_site(web, count = 0, res = None):
    if res is None:
        res = box
    if count == 0:
        return

    phone = input('Введите название продукта для нового сайта: ')
    web_copy = copy.deepcopy(web)
    web_copy['html']['head']['title'] = f'Куплю/продам {phone} недорого'
    web_copy['html']['body']['h2'] = f'У нас самая низкая цена на {phone}'
    res.append((phone, web_copy))
    for p, c in res:
        print(f'Сайт для {p}:\nsite = {c}')
        web_site(web, count - 1)


total = int(input('Сколько сайтов: '))
web_site(site, total)