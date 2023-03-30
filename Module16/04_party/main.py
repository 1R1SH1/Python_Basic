guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

def party():
    while True:
        print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')

        join = input('Гость пришёл или ушёл? ')

        if join == 'пора спать'.lower():
            print('Вечеринка закончилась, все легли спать.')
            break

        name = input('Имя гостя: ')

        if join == 'пришёл'.lower():
            if len(guests) < 6:
                guests.insert(0, name)
                print(f'Привет, {name}!')
            else:
                print(f'Прости, {name}, но мест нет.')
        elif join == 'ушёл'.lower():
            print(f'Пока, {name}!')
            guests.remove(name)


party()
