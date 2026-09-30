def recursive_reverse(some_list):
    """
    Возвращает перевёрнутый список (рекурсивно).
    """
    if len(some_list) <= 1:
        return some_list[:]  
    return [some_list[-1]] + recursive_reverse(some_list[:-1])


if __name__ == "__main__":
    print(recursive_reverse([1, 2, 3, 4, 5]))
    
