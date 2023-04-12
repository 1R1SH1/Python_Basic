def myzip(string, data):
    return ((string[i], data[i]) for i in range(min(len(string), len(data))))


unzip = myzip("abcd", (10, 20, 30, 40))

print('Строка: ' 'abcd', '\nКортеж чисел: ', (10, 20, 30, 40))
print('Результат: ', unzip, *unzip, sep='\n')
