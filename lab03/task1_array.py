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
        result = [list(result) for _ in range(size)]   # list() создаёт независимые копии (не алиасы)
    return result

def pretty_print(arr, indent=0, comma=False):          # comma=True добавляет запятую после закрывающей скобки
    pad = "    " * indent                              # отступ = 4 пробела * уровень
    if not isinstance(arr[0], list):                   # самый глубокий уровень — печатаем в одну строку
        print(pad + str(arr) + ",")                    # запятая после каждого листового списка
    else:
        print(pad + "[")                               # открываем скобку текущего уровня
        for i, item in enumerate(arr):
            is_last = (i == len(arr) - 1)              # определяем последний ли элемент
            pretty_print(item, indent + 1, comma=not is_last)  # все кроме последнего получают запятую
        print(pad + "]" + ("," if comma else ""))      # закрывающая скобка с запятой если не последняя

pretty_print(f1(2, 3))       # рекурсия: 3x3 матрица с 'level 2'
print()
pretty_print(f2(2, 3))       # итерация: 3x3 матрица с 'level 2'
print()
pretty_print(f1(3, 2))       # рекурсия: 2x2x2 куб с 'level 3'
print()
pretty_print(f2(3, 2))       # итерация: 2x2x2 куб с 'level 3'
