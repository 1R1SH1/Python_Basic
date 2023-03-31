letters = input('Введите строку: ')

fragment = letters[letters.find('h') + 1:letters.rfind('h')]
letters = fragment[::-1]

print(letters)
