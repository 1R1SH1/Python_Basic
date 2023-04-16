import random


def luky_num():
    nums, file_l = 0, open('out_file.txt', 'w')

    with file_l as file:
        while nums <= 777:
            user_input = int(input('Введите число: '))
            nums += user_input
            if random.choices((0, 1), (1 - 1 / 13, 1 / 13))[0]:
                raise BaseException('Ой, вам повезло, надо же вы поймали ошибку!')

            print(user_input, file=file)

        print('Вы успешно выполнили условие для выхода из порочного цикла!')

    print_file = open("out_file.txt", "r")
    data = print_file.read()
    print('Содержимое файла out_file.txt: ')
    print(data)
    print_file.close()


luky_num()
