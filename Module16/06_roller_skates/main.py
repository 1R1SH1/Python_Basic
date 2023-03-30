shoes_size = []
feet_size = []
suitable_list = []

skates = int(input('Кол-во коньков: '))
for number in range(skates):
  print(f'Размер {number + 1} пары: ', end = '')
  size = int(input())
  shoes_size.append(size)

people = int(input('Кол-во людей: '))

for number in range(people):
  print(f'Размер ноги  {number + 1},  человека: ', end='')
  size = int(input())
  feet_size.append(size)

for index_shoes in range(skates):
  for index_feet in range(people):
    if shoes_size[index_shoes] >= feet_size[index_feet]:
       suitable_list.append(feet_size[index_feet])

unique_list = list(set(suitable_list))
print(f'Наибольшее кол-во людей, которые могут взять ролики: {len(unique_list)}')
