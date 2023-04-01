user_input = input('Вы готовы заказывать? ')
menu_list = 'утиное филе;фланк-стейк;банановый пирог;плов'

if user_input == 'да':
    print(f'Доступное меню: {format(menu_list)}', f'\nНа данный момент в меню есть: {format(menu_list).split(";")}')
else:
    print('Тогда я подойду позже.')

