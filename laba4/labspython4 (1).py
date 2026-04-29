import io, sys
import functools


def printi(f=None, *, verbose=False):
    """
    Декоратор с опциональным параметром verbose.
    Подавляет print-вывод внутри функции.

    Использование:
        @printi                  — без параметров
        @printi()                — без параметров (со скобками)
        @printi(verbose=True)    — с параметром: выводит захваченный текст в конце
    
    Поддерживает рекурсивные функции: stdout перехватывается только
    на верхнем уровне рекурсии, вложенные вызовы работают корректно.
    """
    def decorator(func):
        # Счётчик глубины рекурсии — список для хранения изменяемого состояния
        # в замыкании (аналог nonlocal для вложенных функций)
        depth = [0]
        # Захваченный поток хранится снаружи wrap, чтобы быть доступным
        # на любом уровне рекурсии
        captured = [None]

        @functools.wraps(func)
        def wrap(*args, **kwargs):
            depth[0] += 1
            # Перехватываем stdout только при первом (внешнем) вызове
            if depth[0] == 1:
                captured[0] = io.StringIO()
                sys.stdout = captured[0]
            try:
                result = func(*args, **kwargs)
            finally:
                depth[0] -= 1
                # Восстанавливаем stdout только когда вышли из внешнего вызова
                if depth[0] == 0:
                    output = captured[0].getvalue()
                    sys.stdout = sys.__stdout__
                    if verbose and output:
                        print(f"[printi captured]:\n{output}", end="")
            return result

        return wrap

    # Поддержка трёх форм применения декоратора:
    #   @printi          → f — это функция, параметры по умолчанию
    #   @printi()        → f=None, возвращаем decorator
    #   @printi(verbose=True) → f=None, возвращаем decorator с параметром
    if f is not None:
        return decorator(f)
    return decorator


# ─── Демонстрация 1: декоратор без параметров ────────────────────────────────

@printi
def hero():
    hp = 100

    def heal(n):
        nonlocal hp
        hp = min(100, hp + n)

    def damage(n):
        nonlocal hp
        hp = max(0, hp - n)

    def get_hp():
        return hp

    print(hp)  # этот print будет подавлен
    return get_hp, heal, damage


get_hp, heal, damage = hero()
damage(30)
heal(20)
damage(80)
print("HP после битвы:", get_hp())  # → 10


# ─── Демонстрация 2: декоратор с verbose=True ─────────────────────────────────

@printi(verbose=True)
def noisy_calc(x):
    print(f"  считаю для {x}...")
    return x * 2


result = noisy_calc(21)
print("Результат noisy_calc:", result)


# ─── Демонстрация 3: рекурсивная функция ──────────────────────────────────────

@printi(verbose=True)
def factorial(n):
    print(f"  factorial({n})")   # print на каждом уровне рекурсии
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # рекурсивный вызов — stdout уже перехвачен


# Все print внутри рекурсии собираются в один буфер и выводятся один раз
result = factorial(5)
print("5! =", result)
