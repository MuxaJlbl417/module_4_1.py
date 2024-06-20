def divide(first, second):
    """
    Деление с проверкой на ноль во втором операнде.
    Возвращает результат деления или строку 'Ошибка'.
    """
    if second == 0:
        return 'Ошибка'
    else:
        return first / second