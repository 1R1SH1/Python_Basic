import os

path = 'C:/Users/Rishat/PycharmProjects/Python_Basic/Module14'

def path_info(path):
    total_size = 0
    path, dirs, files = next(os.walk(path))
    for f in files:
        fp = os.path.join(path, f)
        total_size += os.path.getsize(fp)

    print(path)
    print('Размер каталога (в Кб): ', total_size / 1024)
    print('Количество подкаталогов: ', len(dirs))
    print('Количество файлов: ', len(files))

path_info(path)
