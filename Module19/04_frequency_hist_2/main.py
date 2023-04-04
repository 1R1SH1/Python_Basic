def hist(text_list):
    return {i_letter: text.count(i_letter) for i_letter in text_list}

def invert(invert_keys):
    for i in invert_keys:
        text_dict_invert.setdefault(i, [])
    for key, value in text_dict.items():
        text_dict_invert[value].append(key)

text = input('Введите текст: ')
print()

text_list = sorted(list(set(list(text))))
text_dict = hist(text_list)
print('Оригинальный словарь частот: ')
for k, v in text_dict.items():
     print(f'{k}: {v}')

text_dict_invert = {}
value_num = []
for v in text_dict.values():
    value_num.append(v)
    sort_key = sorted(list(set(value_num)))
invert(sort_key)
print()
print('Инвертированный словарь частот:')
for k, v in text_dict_invert.items():
    print(f'{k}: {v}')
