# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

list_1 = [1, 5, 3]
list_2 = [1, 5, 1, 5]
list_3 = [1, 3, 1, 5, 3, 3]

list_1.extend(list_2)
number_five = list_1.count(5)

list_1.extend(list_3)
number_three = list_1.count(3)

for _ in range(number_five):
    list_1.remove(5)

print(f'Количество цифр 5 при первом объединении: {number_five}', f'\nКоличество цифр 3 при втором объединении: {number_three}', f'\nИтоговый список: {list_1}')
