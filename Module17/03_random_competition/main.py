import random

team_1 = [round(random.uniform(5, 10), 2) for people in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for people in range(20)]

winners = [team_1 if team_1 > team_2 else team_2]

print(f'Первая команда: {team_1}, \nВторая команда: {team_2}, \nПобедители тура: {winners}')

