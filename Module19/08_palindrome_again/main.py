word = input("Введите слово: ")
list_word = list(word)
index = len(list_word)

def check_poli(string):
    k = set()
    count = 0

    for i in range(index // 2):
        if list_word[i] == list_word[index - 1]:
            count += 1

    if count == index // 2:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")

    if count != index // 2:
        for b in list_word:
            if b in k:
                k.remove(b)
            else:
                k.add(b)

        print(('Можно', 'Нельзя')[len(k) > 1], 'сделать полиндром')


def poli(string):
    while True:
        if word.isdigit() == False:
            check_poli(word)
            break
        else:
            print('Можно вводить только буквы!')
            break

poli(word)
