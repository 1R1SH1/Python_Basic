while True:
    ip = input('Введите IP: ')

    if len(ip.split(('.'))) < 4:
        print('Адрес — это четыре числа, разделённые точками.')
    else:
        num_1 = 0
        num_2 = 0
        for x in ip.split('.'):
            if x.isdigit():
                num_1 += 1
                if int(x) > 255:
                    num_2 += 1
                    print(f'{x} превышает 255')
            else:
                print(f'{x} - это не целое число')
        if num_2 == 0 and num_1 == 4:
            print('IP-адрес корректен.')
            break