from Labs05python import gen, reduc, mr


# gen() — генератор, который чередует элементы из нескольких списков

def test_gen_two_lists():
    # [1,2] и [3,4] должны чередоваться: 1,3,2,4
    assert list(gen([1, 2], [3, 4])) == [1, 3, 2, 4]

def test_gen_different_lengths():
    # если один список короче, он просто заканчивается раньше
    assert list(gen([1, 2, 3], [4])) == [1, 4, 2, 3]

def test_gen_empty_list():
    # пустой список не должен ломать генератор
    assert list(gen([], [1, 2])) == [1, 2]

def test_gen_no_args():
    # без аргументов — пустой результат
    assert list(gen()) == []


# reduc() — суммирует числа или склеивает строки через пробел

def test_reduc_numbers():
    assert reduc([1, 2, 3]) == 6

def test_reduc_strings():
    assert reduc(["hello", "world"]) == "hello world"

def test_reduc_empty():
    # пустой список → None
    assert reduc([]) is None


# mr() — объединяет gen() и reduc() вместе

def test_mr_strings():
    # базовый пример из задания
    assert mr(["hello"], ["world"]) == "hello world"

def test_mr_numbers():
    # gen([1,3],[2,4]) → [1,2,3,4] → сумма = 10
    assert mr([1, 3], [2, 4]) == 10

def test_mr_empty():
    assert mr([], []) is None
