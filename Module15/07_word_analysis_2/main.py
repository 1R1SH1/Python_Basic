def polindrom():
  word = input('Введите слово: ')

  if str(word) == str(word)[::-1]:
      print('Cлово является палиндромом')
  else:
      print('Слово не является палиндромом')

polindrom()
