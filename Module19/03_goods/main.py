goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for x in goods:
    key = goods[x]
    calc = store[key]

    each_count = sum(q['quantity'] for q in calc)
    result = sum(p['quantity'] * p['price'] for p in calc)

    print(f'{x} — {each_count} штук, ' 'стоимость {:2.0f} рубля.'.format(result))
