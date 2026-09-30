import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)


# ---------- Классические рекурсивные реализации ----------

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


# ---------- Быстрая пара (F_n, L_n) через деление пополам ----------

def _fib_lucas_pair(n):
    """
    Возвращает кортеж (F_n, L_n), используя рекурсию «разделяй и властвуй».
    Работает за O(log n) благодаря формулам:
        F_{i+j} = (F_i + L_j)(F_i + L_i) / 2
        L_n     = F_{n-1} + F_{n+1}
    """
    if n == 0:
        return (0, 2)
    if n == 1:
        return (1, 1)

    i = n // 2
    j = n - i

    fi, li = _fib_lucas_pair(i)
    fj, lj = _fib_lucas_pair(j)

    # F_n = F_{i+j} = (F_i + L_j)(F_i + L_i) / 2
    fn = (fi + lj) * (fi + li) // 2

    # L_n = F_{n-1} + F_{n+1}
    # F_{n-1} и F_{n+1} получаем через ту же пару (i, j)
    # F_{i+j-1} = (F_i + L_j)(L_i + ... ) — но проще так:
    #   F_{n-1} = F_n - F_{n-2}, а F_{n-2} считаем отдельно нельзя.
    # Поэтому используем другое тождество:
    #   L_n = F_n + 2*F_{n-1}
    # и берём F_{n-1} из пары (i, j-1), если j>=1, либо (i-1, j)
    if j >= 1:
        fj1, _ = _fib_lucas_pair(j - 1)
        # F_{n-1} = F_{i+(j-1)} = (F_i + L_{j-1})(F_i + L_i) / 2
        _, lj1 = _fib_lucas_pair(j - 1)
        fn1 = (fi + lj1) * (fi + li) // 2
    else:
        fi1, _ = _fib_lucas_pair(i - 1)
        _, li1 = _fib_lucas_pair(i - 1)
        # F_{(i-1)+j} = (F_{i-1} + L_j)(F_{i-1} + L_{i-1}) / 2
        fn1 = (fi1 + lj) * (fi1 + li1) // 2

    ln = fn + 2 * fn1

    return (fn, ln)


def fib_with_lucas(n):
    """Быстрое F_n через тождества с числами Люка."""
    return _fib_lucas_pair(n)[0]


def lucas_with_fib(n):
    """Быстрое L_n через тождества с числами Фибоначчи."""
    return _fib_lucas_pair(n)[1]


# ---------- Замер времени и график ----------

def measure(func, n, repeat=1):
    best = float("inf")
    for _ in range(repeat):
        start = time.perf_counter()
        func(n)
        best = min(best, time.perf_counter() - start)
    return best


def run():
    Ns_naive = list(range(0, 31, 2))
    Ns_fast = list(range(0, 41, 2))

    times_naive = [measure(fibonacci, n) for n in Ns_naive]
    times_fast = [measure(fib_with_lucas, n) for n in Ns_fast]

    plt.figure(figsize=(9, 5))
    plt.plot(Ns_naive, times_naive, marker="o", label="fibonacci (наивная)")
    plt.plot(Ns_fast, times_fast, marker="s", label="fib_with_lucas")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение наивной и быстрой реализации Фибоначчи")
    plt.legend()
    plt.grid(True)
    plt.savefig("task4_fib_comparison.png", dpi=120)
    plt.show()

    print("Проверка значений:")
    for n in range(11):
        print(f"n={n}: F={fibonacci(n)}, F_fast={fib_with_lucas(n)}, "
              f"L={lucas(n)}, L_fast={lucas_with_fib(n)}")


if __name__ == "__main__":
    run()