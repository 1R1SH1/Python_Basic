def find_money():
  coin = (x_point ** 2 + y_point ** 2) ** 0.5
  if coin <= r_circle:
    print('\nМонетка где-то рядом')
  else:
    print('\nМонетки в области нет')


print('Введите координаты монетки:')
x_point = float(input('X: '))
y_point = float(input('Y: '))
r_circle = float(input('Введите радиус: '))

find_money()
