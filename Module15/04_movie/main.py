films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
liked_films_list = []
def liked_films():
    user_choose_count = int(input('Сколько фильмов хотите добавить? '))
    for _ in range(user_choose_count):
        user_film = input('Введите название фильма: ')
        if user_film in films:
            liked_films_list.append(user_film)
        else:
            print(f'Ошибка: фильма {user_film} у нас нет :(')

    print(f'Ваш список любимых фильмов: {liked_films_list}')

liked_films()