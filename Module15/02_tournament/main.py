def tournament_net():
    name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
    odd_names_list = []

    for names in range(0, len(name_list), 2):
        odd_names_list.append(name_list[names])
    print('Первый день:', odd_names_list)

tournament_net()