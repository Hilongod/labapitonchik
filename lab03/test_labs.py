import pytest
from io import StringIO
import sys
import importlib.util

spec = importlib.util.spec_from_file_location("labs3python1", "labs3python1_2.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
br, yr, y = mod.br, mod.yr, mod.y

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
    assert y(3, 2.0) == pytest.approx(64.0) 

# --- labs3python1 ---

def capture(func, *args):
    buf = StringIO()
    sys.stdout = buf
    func(*args)
    sys.stdout = sys.__stdout__
    return buf.getvalue()

def test_rec_contains_level():
    assert "level 4" in capture(rec, 4, 2, 0)

def test_mas_contains_level():
    assert "level 4" in capture(mas, 4, 2)

def test_rec_has_brackets():
    out = capture(rec, 4, 2, 0)
    assert "[" in out and "]" in out

def test_mas_has_brackets():
    out = capture(mas, 4, 2)
    assert "[" in out and "]" in out
