import copy
import random
import time
import csv
from sorts.merge import *


SIZES = [10_000, 50_000, 100_000, 250_000, 500_000, 1_000_000, 2_000_000]
RUNS = 3


def time_sort(fn, data):
    arr = copy.copy(data)
    t0 = time.perf_counter_ns()
    fn(arr)
    return (time.perf_counter_ns() - t0) / 1e9


def bench(fn, data):
    times = [time_sort(fn, data) for _ in range(RUNS)]
    return round(sum(times) / len(times), 6)


def run():
    results = []

    for size in SIZES:
        data = [random.randint(0, 10**6) for _ in range(size)]
        print(f"\n--- n={size} ---")

        t_seq = bench(merge_sort, data)
        t_par = bench(merge_sort_parallel, data)

        speedup = t_seq / t_par if t_par > 0 else 0
        print(f"  Secvential: {t_seq:.4f}s")
        print(f"  Paralel:    {t_par:.4f}s")
        print(f"  Speedup:    {speedup:.2f}x")

        results.append([size, t_seq, t_par, round(speedup, 2)])

    with open("results_parallel.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["size", "sequential", "parallel", "speedup"])
        w.writerows(results)

    print("\nSalvat in results_parallel.csv")


if __name__ == "__main__":
    run()