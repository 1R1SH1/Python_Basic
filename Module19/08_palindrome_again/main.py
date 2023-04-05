word = input("Введите слово: ")
list_word = list(word)
index = len(list_word)

def check_poli(string):
    k = set()
    a = 0
    count = 0
    for i in range(index // 2):
        if list_word[i] == list_word[index - 1 - a]:
            count += 1
            a += 1
        if count == index // 2:
            print("Слово является палиндромом")
        else:
            if i in list_word:
                k.remove(i)
            else:
                k.add(i)

    print("Слово не является палиндромом")
    print(('Можно', 'Нельзя')[len(k) > 1], 'сделать полиндром')

def poli(string):
    k = set()
    while True:
      if word.isdigit() == False:
        check_poli(word)
        break
      else:
        print('Можно вводить только буквы!')
        break

poli(word)
