from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        print('Как дела? '), input(' ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        result = func(*args, **kwargs)
        return result

    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
