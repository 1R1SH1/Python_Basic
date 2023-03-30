N = int(input('Количество чисел: '))
numbers = []

for i in range(N):
    user_input = int(input('Число: '))
    numbers.append(user_input)
print (f'Последовательность: {numbers}')

for i in range(len(numbers)):
    if numbers[i:] == numbers[i:][::-1]:
        print(f'Нужно приписать чисел: {i}')
        print(f'Сами числа: {numbers[:i][::-1]}')
        break
