class_1 = []
class_2 = []

for i in range(160, 176 + 2, 2):
  class_1.append(i)

for j in range(162, 180 + 3, 3):
  class_2.append(j)

class_1.extend(class_2)

print(f'Отсортированный список учеников: {sorted(class_1)}')
