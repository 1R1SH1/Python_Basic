def divider():
  user_number = int(input('Введите число: '))
  number = 2

  while user_number % number != 0:
    number += 1

  print('Наименьший делитель, отличный от единицы:', number)

divider()


