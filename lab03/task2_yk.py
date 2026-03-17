# Задача 2: расчёт y_k = b_k * y_{k-1}
# y_0 = 1,  b_0 = 1/(2x),  b_k = b_{k-1} * x²

def c1(k, x):
    if x == 0:                                         # деление на ноль недопустимо
        raise ValueError("x не должен быть равен нулю")
    if k < 0:                                          # отрицательный шаг не определён
        raise ValueError("k должен быть >= 0")
    def _b(s): return 1/(2*x) if s == 0 else _b(s-1) * x**2  # b_0=1/(2x), b_k=b_{k-1}*x²
    def _y(s): return 1.0 if s == 0 else _b(s) * _y(s-1)     # y_0=1, y_k=b_k*y_{k-1}
    return _y(k)

def c2(k, x):
    if x == 0:                                         # деление на ноль недопустимо
        raise ValueError("x не должен быть равен нулю")
    if k < 0:                                          # отрицательный шаг не определён
        raise ValueError("k должен быть >= 0")
    b, y = 1 / (2 * x), 1.0                           # начальные значения b_0 и y_0
    for _ in range(1, k + 1):                         # итерируемся от 1 до k
        b = b * x**2                                   # b_k = b_{k-1} * x²
        y = b * y                                      # y_k = b_k * y_{k-1}
    return y

for k in range(5):
    print(f"k={k}: Result={c1(k, 2.0)}  Result2={c2(k, 2.0)}")
