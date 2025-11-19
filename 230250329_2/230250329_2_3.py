import random


def issue3() -> tuple:
    r = random.randint(1, 10)
    h = random.randint(1, 10)
    V = 1 / 3 * 3.14 * r**2 * h
    return [V, r, h]


[V, r, h] = issue3()
print(f"高为 {h}，底面半径为 {r} 的圆锥体积为：{V:.2f}")
