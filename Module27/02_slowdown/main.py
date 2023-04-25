import time
from typing import Callable, Any

def waiting(func: Callable) -> Callable:
  def wrapped_func(*args, **kwargs) -> Any:
    print('Идёт загрузка...ждите!')
    time.sleep(3)
    result = func(*args, **kwargs)
    return result
  return wrapped_func

@waiting
def sum(a, b):
  return a + b
@waiting
def test():
  print('Загрузка завершена!')

print(sum(1, 2))
test()
