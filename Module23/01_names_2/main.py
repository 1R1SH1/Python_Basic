def name_checker(data):
  with open('people.txt', encoding='UTF-8') as people_l:
    try:
        people_l = people_l.readlines()
        size = sum([len(i.strip()) for i in people_l])
        for x, i in enumerate(people_l, 1):
            if len(i.strip()) < 3:
                raise BaseException(f'Ошибка: менее трёх символов в строке {x}')
    except BaseException as exp:
        print(exp)
    finally:
        print('Общее количество символов:', size)

name_checker('people.txt')
