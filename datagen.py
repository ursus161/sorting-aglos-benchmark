import random

def gen_random(n):
    return [random.randint(0, n * 10) for _ in range(n)]

def gen_sorted(n):
    return list(range(n))

def gen_reversed(n):
    return list(range(n, 0, -1))

def gen_nearly_sorted(n):
    arr = list(range(n))
    for _ in range(n // 20):
        i = random.randint(0, n - 2)
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def gen_duplicates(n):
    vals = [random.randint(0, 10) for _ in range(10)]
    return [random.choice(vals) for _ in range(n)]


