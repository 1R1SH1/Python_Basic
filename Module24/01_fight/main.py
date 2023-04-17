import random

class Warrior:
  def __init__(self):
    self.hp_warrior = 0

warrior_1 = Warrior()
warrior_2 = Warrior()
warrior_1.hp_warrior = 100
warrior_2.hp_warrior = 100

while True:
  who_beats = random.randint(0, 10)
  if warrior_1.hp_warrior == 0:
    print('Победил Ришат')
    break
  elif warrior_2.hp_warrior == 0:
    print('Победил Куратор')
    break
  elif who_beats < 6:
    warrior_2.hp_warrior -= 20
    print('Куратор дубасит Ришата')
    print(f'У Ришата осталось {warrior_2.hp_warrior} здоровья\n')
  elif who_beats > 5:
    warrior_1.hp_warrior -= 20
    print('Ришат лупит Куратора')
    print(f'У Куратора осталось {warrior_1.hp_warrior} здоровья\n')
