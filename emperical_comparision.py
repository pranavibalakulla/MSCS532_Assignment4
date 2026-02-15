import random
import time
import sys
from statistics import median

# ----------------------------
# Sorting implementations
# ----------------------------

def heapsort(arr):
    a = arr[:]  # work on a copy for fair comparisons
    n = len(a)

    def heapify(n, i):
        # iterative heapify (sift down) to keep aux space O(1)
        while True:
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and a[l] > a[largest]:
                largest = l
            if r < n and a[r] > a[largest]:
                largest = r

            if largest == i:
                break
            a[i], a[largest] = a[largest], a[i]
            i = largest

    # Build max-heap: O(n)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extract elements: n times * O(log n)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        heapify(end, 0)

    return a


def mergesort(arr):
    # returns a new sorted list
    n = len(arr)
    if n <= 1:
        return arr[:]

    mid = n // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    # merge step: O(n)
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def quicksort(arr):
    # randomized pivot to avoid worst-case on sorted inputs (expected O(n log n))
    a = arr[:]
    def _qs(lo, hi):
        if lo >= hi:
            return
        pivot_idx = random.randint(lo, hi)
        a[pivot_idx], a[hi] = a[hi], a[pivot_idx]
        pivot = a[hi]

        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]

        _qs(lo, i - 1)
        _qs(i + 1, hi)

    _qs(0, len(a) - 1)
    return a


# ----------------------------
# Benchmarking utilities
# ----------------------------

def generate_data(n, dist, seed=123):
    random.seed(seed)
    if dist == "random":
        return [random.randint(0, 10**7) for _ in range(n)]
    if dist == "sorted":
        return list(range(n))
    if dist == "reverse":
        return list(range(n, 0, -1))
    raise ValueError("Unknown distribution")


def time_one(sort_fn, data, repeats=5):
    times = []
    for _ in range(repeats):
        arr = data[:]  # fresh copy each run
        start = time.perf_counter()
        out = sort_fn(arr)
        end = time.perf_counter()
        # correctness check (lightweight)
        if out != sorted(data):
            raise AssertionError(f"{sort_fn.__name__} produced incorrect output.")
        times.append(end - start)
    return median(times)


def run_benchmarks(sizes, dists, repeats=5):
    algorithms = [
        ("Heapsort", heapsort),
        ("Quicksort", quicksort),
        ("MergeSort", mergesort),
    ]

    results = []  # list of dict rows
    for n in sizes:
        for dist in dists:
            data = generate_data(n, dist, seed=123)  # same base data per (n, dist)
            for name, fn in algorithms:
                t = time_one(fn, data, repeats=repeats)
                results.append({
                    "n": n,
                    "distribution": dist,
                    "algorithm": name,
                    "median_seconds": t
                })
    return results


def print_table(results):
    # simple grouped print
    results_sorted = sorted(results, key=lambda x: (x["n"], x["distribution"], x["algorithm"]))
    print(f"{'Input Size':<12}  {'Distribution':<15}  {'Algorithm':<15}  {'Execution Time(s)':<20}")
    print("-" * 65)
    for r in results_sorted:
        print(f"{r['n']:<12}  {r['distribution']:<15}  {r['algorithm']:<15}  {r['median_seconds']:<20.6f}")


if __name__ == "__main__":
    # If recursion is an issue for quicksort on very large n, you can increase recursion limit:
    sys.setrecursionlimit(10**7)

    sizes = [1000, 2000, 5000, 10000, 20000]  # adjust as needed
    dists = ["sorted", "reverse", "random"]
    repeats = 5

    results = run_benchmarks(sizes, dists, repeats=repeats)
    print_table(results)