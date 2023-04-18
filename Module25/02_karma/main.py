import random

class __KillError(Exception):
    pass

class __DrunkError(Exception):
    pass

class __CarCrashError(Exception):
    pass

class __GluttonyError(Exception):
    pass

class __DepressionError(Exception):
    pass

def life_simulater():
    karma = 0
    with open('karmaLog.txt', 'w') as log:
        while karma < 500:
            try:
                not_lucky = random.choices((0, 1), (1 - 1 / 10, 1 / 10))[0]

                if not_lucky:
                    raise Exception
                else:
                    karma += random.randint(1, 7)
                    print(f'Карма = {karma}')
            except Exception:
                log.write(str(random.choice(
                    [__DepressionError, __GluttonyError, __CarCrashError, __KillError, __DrunkError])) + '\n')

        print('Вы достигли просветления!')

life_simulater()
