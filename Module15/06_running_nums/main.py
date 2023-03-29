def shift():
    list = []
    numbers = int(input('Введите кол-во символов в списке: '))
    for _ in range(numbers):
        user_number = int(input('Введите число: '))
        list.append(user_number)
    shifting = int(input('Сдвиг: '))

    new_list = []
    for number in range(len(list)):
        new_list.append(list[number - shifting])

    print(f'Изначальный список: {list}', f'\nСдвинутый список: {new_list}')

shift()
