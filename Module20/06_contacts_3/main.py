def add_contact():
  name = tuple(input('Введите имя и фамилию нового контакта (через пробел):').split())
  if name in phone_book:
    print('Такой человек уже есть в контактах.')
  else:
    phone = input('Введите номер телефона: ')
    phone_book[name] = phone
    print(f'Текущий словарь контактов: {phone_book}')

def search_contact():
  search = input('Введите фамилию для поиска: ')
  for item, number in phone_book.items():
    if search == item[1]:
      print(item, number)
      break

phone_book = dict()
while True:
  action = int(input('Введите номер действия: \n1. Добавить контакт  \n2. Найти человека '))
  if action == 1:
    add_contact()
  elif action == 2:
    search_contact()
