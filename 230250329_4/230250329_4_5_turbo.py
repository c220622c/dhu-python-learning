import time
import os
from concurrent.futures import ThreadPoolExecutor

CPU_COUNT = os.cpu_count() or 8
OPTIMAL_THREADS = CPU_COUNT * 2
def find_narcissus_smart(n:int) -> list:
    result = []
    hashmap = []
    for i in range(10):
        hashmap.append(i**n)
    for i in range(10**(n-1),10**n):
        add_up = 0
        str_i = str(i)
        for j in str_i:
            add_up =add_up+hashmap[int(j)]
        if add_up == i:
            result.append(i)
    return result

def find_narcissus(n:int) -> list:
    result = []
    for i in range(10**(n-1),10**n):
        str_i = str(i)
        add_up = 0
        for j in range(len(str_i)):
            add_up = add_up+int(str_i[j])**n
        if add_up == i:
            result.append(i)
    return result
def _worker(n: int, start: int, end: int) -> list:
    result = []
    hashmap = [i**n for i in range(10)]
    for i in range(start, end):
        add_up = sum(hashmap[int(d)] for d in str(i))
        if add_up == i:
            result.append(i)
    return result

def find_narcissus_turbo(n: int, num_threads: int = None) -> list:
    if num_threads is None:
        num_threads = OPTIMAL_THREADS
    
    start_range = 10**(n-1)
    end_range = 10**n
    chunk_size = (end_range - start_range) // num_threads
    
    ranges = []
    for i in range(num_threads):
        start = start_range + i * chunk_size
        end = start_range + (i + 1) * chunk_size if i < num_threads - 1 else end_range
        ranges.append((n, start, end))
    
    result = []
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(_worker, *r) for r in ranges]
        for future in futures:
            result.extend(future.result())
    
    return sorted(result)

if __name__ == "__main__":
    print(f"CPU: {CPU_COUNT}核 | 线程: {OPTIMAL_THREADS}")

    for i in range(1, 10):
        start = time.time()
        find_narcissus(i)
        end = time.time()
        print(f"n={i}, 普通方法: {end - start:.4f}秒")

        start = time.time()
        find_narcissus_smart(i)
        end = time.time()
        print(f"n={i}, 优化方法: {end - start:.4f}秒")

        start = time.time()
        find_narcissus_turbo(i)
        end = time.time()
        print(f"n={i}, 极速方法: {end - start:.4f}秒")

