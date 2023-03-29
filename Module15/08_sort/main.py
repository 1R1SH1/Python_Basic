numbers_list = []
new_number_list = []

def sorted_list():
    numbers_count = int(input('Введите количество чисел: '))
    count = 0

    for _ in range(0, numbers_count):
        count += 1
        to_list = int(input(f'Введите {count}-е число: '))
        numbers_list.append(to_list)
        new_number_list.append(to_list)
        len_number_list = len(numbers_list)
    for i in range(1, len_number_list):
        for j in range(len_number_list - 1, i - 1, -1):
            if numbers_list[j - 1] > numbers_list[j]:
                numbers_list[j - 1], numbers_list[j] = numbers_list[j], numbers_list[j - 1]

    print(f'Изначальный список: {new_number_list}', f'\nОтсортированный список: {numbers_list}')

sorted_list()