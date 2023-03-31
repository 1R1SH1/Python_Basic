letters = ('а', 'е', 'и', 'о', 'у', 'ё', 'ю', 'я')

user_input = input('Введите текст: ')

list_letters = [x for x in user_input if x in letters]

print(f'Список гласных букв: {list_letters}', f'\nДлина списка: {len(list_letters)}')