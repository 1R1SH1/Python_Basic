first_s = input('Введите первую стоку: ')
second_s = input('Введите вторую строку: ')
k = second_s.index(second_s[0]) + first_s.index(second_s[0])

for position in range(len(second_s)):
  if second_s[position] != first_s[(position + k) % len(second_s)]:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
    break
else:
  print('Первая строка получается из второй со сдвигом ', k)
