from math import inf

def divide(first, second):
    """
    Деление с проверкой на ноль во втором операнде.
    Возвращает результат деления или бесконечность.
    """
    if second == 0:
        return inf
    else:
        return first / second