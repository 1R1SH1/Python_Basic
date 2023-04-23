import functools
import datetime
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """
    Декоратор. Логирует ошибки функций с указанием даты и времени возникновения.
    """

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print('Функция: ', func.__name__)
            print('Документация: ', func.__doc__)
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            string = '{} - {}:\t{}\n'.format(datetime, func.__name__, ex)
            with open('function_errors.log', 'a', encoding='utf-8') as log:
                log.write(string)

    return wrapped_func


@logging
def division_by_zero():
    """Деление на нуль."""
    return 5 / 0


@logging
def value_error():
    """Вызывает ValueError."""
    raise ValueError('Неверное значение')


@logging
def name_error():
    """Вызывает NameError."""
    raise NameError('Неверное имя')


@logging
def index_error():
    """Вызывает IndexError."""
    raise IndexError('Нет такого индекса')


@logging
def squares_sum() -> int:
    """
    Функция нахождения суммы квадратов
    для каждого N от 0 до заданного числа,
    где 0 <= N <= 100

    :return: сумма квадратов
    """
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(10000)])
    return result


division_by_zero()
value_error()
name_error()
index_error()
myfunc = squares_sum()
print(myfunc)
