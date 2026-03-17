# Задача 1: создание n-мерного массива

def f1(n, size, _label=None):
    if n < 1 or size < 1:                              # проверка входных данных
        raise ValueError("n и size должны быть >= 1")
    if _label is None:                                 # запоминаем исходный n при первом вызове
        _label = n
    if n == 1:                                         # база рекурсии — список строк-листьев
        return [f"level {_label}"] * size
    return [f1(n - 1, size, _label) for _ in range(size)]  # рекурсия вглубь

def f2(n, size):
    if n < 1 or size < 1:                              # проверка входных данных
        raise ValueError("n и size должны быть >= 1")
    result = [f"level {n}"] * size                     # начинаем с одномерного списка
    for _ in range(n - 1):                             # (n-1) раз оборачиваем в новый уровень
        result = [list(result) for _ in range(size)]   # list() создаёт независимые копии
    return result

print(f1(2, 3))  # ожидаем: 3x3 матрица с 'level 2'
print(f2(2, 3))

print(f1(3, 2))  # ожидаем: 2x2x2 куб с 'level 3'
print(f2(3, 2))
