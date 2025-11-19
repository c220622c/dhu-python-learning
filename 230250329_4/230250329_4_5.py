import time


def find_narcissus(n: int) -> list:
    result = []
    for i in range(10 ** (n - 1), 10**n):
        str_i = str(i)
        add_up = 0
        for j in range(len(str_i)):
            add_up = add_up + int(str_i[j]) ** n
        if add_up == i:
            result.append(i)
    return result


def find_narcissus_smart(n: int) -> list:
    result = []
    hashmap = []
    for i in range(10):
        hashmap.append(i**n)
    for i in range(10 ** (n - 1), 10**n):
        add_up = 0
        str_i = str(i)
        for j in str_i:
            add_up = add_up + hashmap[int(j)]
        if add_up == i:
            result.append(i)
    return result


# 存储时间数据
n_values = []
time_normal = []
time_smart = []

for i in range(1, 10):
    n_values.append(i)

    start = time.time()
    find_narcissus(i)
    end = time.time()
    time_normal.append(end - start)

    start = time.time()
    find_narcissus_smart(i)
    end = time.time()
    time_smart.append(end - start)
print("n | 普通算法 | 优化算法")
print("--------------------")
for n in n_values:
    print(f"{n} | {time_normal[n - 1]:.4f}s | {time_smart[n - 1]:.4f}s")
