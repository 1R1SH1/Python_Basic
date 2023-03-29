def even_numbers():
    user_num = int(input('Введите число: '))
    odd_numbers_list = []

    for numbers in range(1, user_num + 1):
        if numbers % 2 == 1:
            odd_numbers_list.append(numbers)
    print('Список из нечётных чисел от одного до N:', odd_numbers_list)

even_numbers()
