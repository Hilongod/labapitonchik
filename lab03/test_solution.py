import pytest
from task1_array import f1, f2
from task2_yk    import c1, c2

ARRAY_FUNCS = [f1, f2]
YK_FUNCS    = [c1, c2]

def depth(a):                                          # глубина вложенности списка
    return 0 if not isinstance(a, list) else 1 + depth(a[0])

def leaves_ok(a, n):                                   # все листья равны "level n"
    return all(leaves_ok(x, n) for x in a) if isinstance(a, list) else a == f"level {n}"

# ── Тесты задачи 1 ────────────────────────────────────────────

@pytest.mark.parametrize("f", ARRAY_FUNCS)
def test_1d(f):                                        # 1-мерный массив — плоский список нужной длины
    r = f(1, 4)
    assert len(r) == 4 and all(x == "level 1" for x in r)

@pytest.mark.parametrize("f", ARRAY_FUNCS)
def test_2d(f):                                        # 2-мерный: глубина=2, все размеры=size
    r = f(2, 3)
    assert depth(r) == 2 and len(r) == 3 and all(len(row) == 3 for row in r)

@pytest.mark.parametrize("f", ARRAY_FUNCS)
def test_3d(f):                                        # 3-мерный: глубина=3
    r = f(3, 2)
    assert depth(r) == 3 and len(r) == 2 and len(r[0][0]) == 2

@pytest.mark.parametrize("f", ARRAY_FUNCS)
@pytest.mark.parametrize("n,size", [(1,1),(2,5),(3,3)])
def test_labels(f, n, size):                           # метки листьев соответствуют исходному n
    assert leaves_ok(f(n, size), n)

@pytest.mark.parametrize("f", ARRAY_FUNCS)
def test_no_aliases(f):                                # подсписки — независимые объекты в памяти
    r = f(2, 3)
    assert r[0] is not r[1]

@pytest.mark.parametrize("f", ARRAY_FUNCS)
@pytest.mark.parametrize("n,size", [(0,3),(2,0),(-1,2)])
def test_array_invalid(f, n, size):                    # неверные аргументы → ValueError
    with pytest.raises(ValueError):
        f(n, size)

def test_array_both_equal():                           # рекурсия и итерация дают одинаковый результат
    for n, size in [(1,3),(2,3),(3,2)]:
        assert f1(n,size) == f2(n,size)

# ── Тесты задачи 2 ────────────────────────────────────────────

def ref(k, x): return x**(k*k) / 2**k                 # закрытая формула y_k = x^(k²) / 2^k

@pytest.mark.parametrize("f", YK_FUNCS)
def test_k0(f):                                        # y_0 = 1 для любого x
    assert f(0, 2.0) == pytest.approx(1.0)

@pytest.mark.parametrize("f", YK_FUNCS)
@pytest.mark.parametrize("k,x", [(1,2.0),(2,2.0),(3,2.0),(1,-1.5),(4,0.5)])
def test_yk_formula(f, k, x):                          # совпадение с закрытой формулой x^(k²)/2^k
    assert f(k, x) == pytest.approx(ref(k, x), rel=1e-9)

@pytest.mark.parametrize("f", YK_FUNCS)
def test_x_zero(f):                                    # x=0 → ValueError
    with pytest.raises(ValueError): f(2, 0)

@pytest.mark.parametrize("f", YK_FUNCS)
def test_negative_k(f):                                # k<0 → ValueError
    with pytest.raises(ValueError): f(-1, 2.0)

def test_yk_both_equal():                              # рекурсия и итерация дают одинаковый результат
    for k in range(6):
        for x in [2.0, -1.5, 0.5]:
            assert c1(k,x) == pytest.approx(c2(k,x), rel=1e-9)
