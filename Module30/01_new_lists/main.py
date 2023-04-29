from typing import List
import functools


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

print(list(map(lambda x: float('{:.3f}'.format(x ** 3)), floats)))
print(list(filter(lambda x: len(set(x)) >= 5, names)))
print(functools.reduce(lambda x, y: x * y, numbers))
