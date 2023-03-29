store = []

def sorted_store():
  container_count = int(input('Количество контейнеров: '))

  for _ in range(container_count):
    container_count += 1
    weight = int(input('Введите вес контейнера: '))
    if weight <= 200:
      store.append(weight)
    else:
      print('Вес контейнера не должен превышать 200 кг')

  new_container_weight = int(input('Введите вес нового контейнера: '))
  place = 0

  while place < len(store) and store[place] >= new_container_weight:
    place += 1
  print('\nНомер, куда встанет контейнер:', place + 1)

sorted_store()