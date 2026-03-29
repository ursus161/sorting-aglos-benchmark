import copy
import csv
import sys
import time

from datagen import *
from sorts.bubble import bubble_sort
from sorts.cocktail import cocktail_sort
from sorts.insertion import insertion_sort
from sorts.merge import merge_sort
from sorts.heap import heap_sort
from sorts.radix import radix_sort


SIZES = [500, 1000, 2000, 3000, 5000]
RUNS = 3

DATA_TYPES = {
    "random": gen_random,
    "sorted": gen_sorted,
    "reversed": gen_reversed,
    "nearly_sorted": gen_nearly_sorted,
    "duplicates": gen_duplicates,
}

ALGORITHMS = {
    "BubbleSort":   bubble_sort,
    "CocktailSort": cocktail_sort,
    "InsertionSort":insertion_sort,
    "MergeSort":    merge_sort,
    "HeapSort":     heap_sort,
    "RadixSort":    radix_sort,
    "sorted()":     None,
}


def time_sort(fn, data):
    arr = copy.copy(data)
    t0 = time.perf_counter_ns()
    sorted(arr) if fn is None else fn(arr)
    return (time.perf_counter_ns() - t0) / 1e9


def bench(fn, data):
    times = [time_sort(fn, data) for _ in range(RUNS)]
    return round(sum(times) / len(times), 6)


def run():
    results = []

    for dtype, gen in DATA_TYPES.items():
        for size in SIZES:
            data = gen(size)
            print(f"\n--- {dtype} | n={size} ---")

            for name, fn in ALGORITHMS.items():
                avg = bench(fn, data)
                print(f"  {name:15s} | {avg:.6f}s")
                results.append([name, dtype, size, avg])

    with open("results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["algorithm", "data_type", "size", "avg_time_s"])
        w.writerows(results)

    print("\nSalvat in results.csv")


if __name__ == "__main__":
    run()