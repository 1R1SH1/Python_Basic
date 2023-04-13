def sum(data):
    result = 0
    for dat in data:
        if isinstance(dat, list):
            result += sum(dat)
        else:
            result += dat
    return result

data_1 = [[1, 2, [3]], [1], 3]
data_2 = (1, 2, 3, 4, 5)

res = sum(data_1)
res_2 = sum(data_2)
print(f'Ответ в консоли: {res}', f'\nОтвет в консоли: {res_2}')
