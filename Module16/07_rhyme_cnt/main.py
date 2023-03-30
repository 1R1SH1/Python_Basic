N = int(input("Кол-во человек: "))
K = int(input("Какое число в считалке? "))
print("Значит, выбывает каждый", K, "человек.")
people = list(range(1, N + 1))
out = 0

for i in range(N - 1):
    print('Текущий круг людей', people)
    start_count = out % len(people)
    out = (start_count + K - 1) % len(people)

    print('Начало счёта с номера', people[start_count])
    print('Выбывает человек под номером', people[out])
    people.remove(people[out])

print()

print('Остался человек под номером', people[0])
