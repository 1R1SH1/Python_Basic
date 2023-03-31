def ceasar_encode(letter, shift):
    if letter.isalpha():
        number = ord(letter) + shift % 32
        if number > 1103:
            number -= 32
        return chr(number)
    return letter

words = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

for l in words:
    print(ceasar_encode(l, shift), end='')