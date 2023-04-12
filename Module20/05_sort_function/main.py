tpl = (6, 3, -1, 8, 4, 10, -5)

def sort(data):
  new_tpl = data[:]

  if all(type(item) is int for item in new_tpl):
    return sorted(new_tpl)
  else:
    return new_tpl

print('Отсортировано: ', sort(tpl))
