phones = ['9999999999', '999999-999', '99999x9999']

def check_phones(data):
    names_list = ['первый номер:', 'второй номер:', 'третий номер:']
    count = -1
    for numbers in data:
        count += 1
        if numbers.startswith(('8','9')) and len(numbers) == 10 and all(map(str.isdigit, numbers)):
            print(names_list[count], 'всё в порядке')
        else:
            print(names_list[count], 'не подходит')

check_phones(phones)
