def input_gpu():
    gpu_list = []
    gpus = int(input('Введите количество видеокарт: '))

    for _ in range(gpus):
        add_gpu = int(input(f'{_ + 1} Видеокарта: '))
        gpu_list.append(add_gpu)

    return gpu_list

def calc_gpu(old_gpu_store):
    new_gpu_list = []

    for gpu_store in range(len(old_gpu_store)):
        if old_gpu_store[0] >= old_gpu_store[gpu_store]:
            new_gpu_list.append(old_gpu_store[gpu_store])

    print('\nСтарый список видеокарт:', old_gpu_store, '\nНовый список видеокарт:', new_gpu_list)

old_gpu_store = input_gpu()
calc_gpu(old_gpu_store)
