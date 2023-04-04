num = int(input('Введите количество пар слов: '))
print()
dict = dict()

for i_num in range(num):
    word_list = input(f'{i_num + 1} пара: ').split()
    dict[word_list[0]] = word_list[2]
while True:
    word = input('\nВведите слово: ').title()
    print()
    for i_word in dict.items():
        if word in i_word[0]:
            print('Синоним -', i_word[1])
            break
        elif word in i_word[1]:
            print('Синоним -', i_word[0])
            break
    else:
        print(f'\nТакого слова в словаре нет.')
