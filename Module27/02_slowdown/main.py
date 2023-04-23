import time
from typing import Callable, Any

def waiting(func: Callable) -> Callable:
  def timing() -> Any:
    print('Идёт загрузка...ждите!')
    time.sleep(3)
    func()
  return timing

@waiting
def test():
  print('Загрузка завершена!')

test()
