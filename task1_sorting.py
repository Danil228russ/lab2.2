import time
import random
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def quick_sort(arr):
    a = arr.copy()
    _quick_sort(a, 0, len(a) - 1)
    return a


def _quick_sort(a, low, high):
    if low < high:
        p = _partition(a, low, high)
        _quick_sort(a, low, p - 1)
        _quick_sort(a, p + 1, high)


def _partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def measure(func, data):
    start = time.perf_counter()
    func(data)
    return time.perf_counter() - start


def run_experiments():
    sizes = [100, 200, 400, 800, 1600, 3200]
    results = {
        "random": {"selection": [], "quick": []},
        "sorted": {"selection": [], "quick": []},
        "reversed": {"selection": [], "quick": []},
    }

    for n in sizes:
        random_data = [random.randint(0, 10000) for _ in range(n)]
        sorted_data = list(range(n))
        reversed_data = list(range(n, 0, -1))

        for name, data in [("random", random_data),
                           ("sorted", sorted_data),
                           ("reversed", reversed_data)]:
            results[name]["selection"].append(measure(selection_sort, data))
            results[name]["quick"].append(measure(quick_sort, data))

    # Графики
    for name in results:
        plt.figure(figsize=(8, 5))
        plt.plot(sizes, results[name]["selection"], marker="o",
                 label="Selection Sort")
        plt.plot(sizes, results[name]["quick"], marker="s",
                 label="Quick Sort")
        plt.xlabel("Размер массива (n)")
        plt.ylabel("Время выполнения (сек)")
        plt.title(f"Зависимость времени сортировки от размера\nДанные: {name}")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"task1_{name}.png", dpi=120)
        plt.show()


if __name__ == "__main__":
    run_experiments()