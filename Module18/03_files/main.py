word = input('Введите название файла: ')
if word.startswith(tuple('@№$%^&*()')):
  print('Ошибка: название начинается на один из специальных символов.')
elif word.endswith('.docx'):
  print('Файл назван верно.')
elif word.endswith('.txt'):
  print('Файл назван верно.')
else:
  print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
