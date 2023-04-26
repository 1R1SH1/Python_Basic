import math


class MyMath:
    def circle_len(radius):
        return (2 * math.pi * radius)

    def circle_sq(radius):
        return (math.pi * radius ** 2)

    def cube_volume(side):
        return (side ** 3)

    def sfer_ground_sq(radius):
        return (4 * math.pi * radius ** 2)


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(side=5)
res_4 = MyMath.sfer_ground_sq(radius=5)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
