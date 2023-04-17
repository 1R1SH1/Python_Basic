class Parents:
  def __init__(self, name, age, childs):
    self.name, self.age, self.childs = name, age, childs

  def __str__(self):
    return self.name + ' ' + str(self.age) + '\n' + '\n'.join([str(x) for x in self.childs])

  def calm(self, child):
    for x in self.childs:
      if x is child:
        x.is_calm = True

  def feed(self, child):
    for x in self.childs:
      if x is child:
        x.is_fed = True

class Child:
  def __init__(self, name, age, is_calm, is_fed):
    self.name, self.age, self.is_calm, self.is_fed = name, age, is_calm, is_fed

  def __str__(self):
    return self.name + ' ' + str(self.age) + ' лет ' + ('Спокоен ' if self.is_calm else 'Раздражен ') + ('Сыт' if self.is_fed else 'Голоден')

ivan = Child('Иван', 10, True, False)
alina = Child('Алина', 7, False, False)
mom = Parents('Наташа', 25, [ivan, alina])

print(mom)
mom.calm(alina)
print(mom)
mom.feed(alina)
print(mom)
mom.feed(ivan)
print(mom)
