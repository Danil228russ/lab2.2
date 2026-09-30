def tribonacci(n):
    """
    Рекурсивная функция для n-го числа Трибоначчи.
    T(0)=0, T(1)=0, T(2)=1, T(n)=T(n-1)+T(n-2)+T(n-3)
    """
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


if __name__ == "__main__":
    print([tribonacci(i) for i in range(10)])
  