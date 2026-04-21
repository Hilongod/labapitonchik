import pytest
from io import StringIO
import sys

from labs3python1_2 import br, yr, y
from labs3python1 import rec, mas

# --- labs3python1_2 ---

def test_br_base():
    assert br(0, 2.0) == 1 / (2 * 2.0)

def test_br_k1():
    assert br(1, 2.0) == br(0, 2.0) * 2.0**2

def test_yr_base():
    assert yr(0, 2.0) == 1

def test_yr_matches_y():
    assert yr(3, 2.0) == y(3, 2.0)

def test_y_result():
    assert y(3, 2.0) == pytest.approx(32.0)

# --- labs3python1 ---

def capture(func, *args):
    buf = StringIO()
    sys.stdout = buf
    func(*args)
    sys.stdout = sys.__stdout__
    return buf.getvalue()

def test_rec_and_mas_same_output():
    assert capture(rec, 4, 2, 0) == capture(mas, 4, 2).strip()

def test_rec_contains_level():
    assert "level 4" in capture(rec, 4, 2, 0)

def test_mas_contains_level():
    assert "level 4" in capture(mas, 4, 2)
