def summ(number):
  summ = 0
  while number > 0:
    summ += int(number % 10)
    number //= 10
  return summ

def count(number):
  count = 0
  while number > 0:
    count += int(1)
    number = (number // 10) - 1
  return count

number = int(input('Введите число: '))

print('\nСумма чисел: ', summ(number), '\nКоличество цифр в числе: ', count(number), '\nРазность суммы и количества цифр:: ', summ(number) - count(number))

