user_input = int(input('Введите длну списка: '))

list_numbers = [N % 5 if N % 2 else 1 for N in range(user_input)]

print(list_numbers)
