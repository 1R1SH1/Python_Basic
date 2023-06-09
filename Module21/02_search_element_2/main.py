import random

site = {
'html': {
'head': {
'title': 'Мой сайт'
},
'body': {
'h2': 'Здесь будет мой заголовок',
'div': 'Тут, наверное, какой-то блок',
'p': 'А вот здесь новый абзац'
}
}
}

def find_key(struct, key, depth, depth_2):
  if key in struct:
    return struct[key]
  if depth > 1:
    for sub_struct in struct.values():
      if isinstance(sub_struct, dict):
        result = find_key(sub_struct, key, depth - 1, depth_2)
      else:
        result = None
    return result


user_key = input("Какой ключ ищем? ")
max_depth = input("Хотите ввести максимальную глубину? Y/N:").lower()

if max_depth == "y":
  search_depth = int(input("Введите максимальную глубину: "))
  value = find_key(site, user_key, search_depth, max_depth)
  print("Значение ключа: ", value)
elif max_depth == "n":
  search_depth = random.randint(2, 10)
  value = find_key(site, user_key, search_depth, max_depth)
  print("Значение ключа: ", value)
