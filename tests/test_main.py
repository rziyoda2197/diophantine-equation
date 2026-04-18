import pytest
from your_module import diophantine

def test_diophantine():
    assert diophantine(2, 3, 12) == [(3, 2)]
    assert diophantine(30, 12, -18) == [(-3, 8)]
    assert diophantine(1, 1, 1) == [(1, 0), (0, 1)]
    assert diophantine(2, 2, 1) == []
    assert diophantine(1, 0, 2) == [(2, 0)]
    assert diophantine(0, 1, 3) == [(0, 3)]

def test_diophantine_invalid_input():
    with pytest.raises(TypeError):
        diophantine('a', 2, 3)
    with pytest.raises(TypeError):
        diophantine(1, 'b', 3)
    with pytest.raises(TypeError):
        diophantine(1, 2, 'c')

def test_diophantine_zero_coefficients():
    assert diophantine(0, 0, 1) == []
    assert diophantine(0, 0, 0) == [(0, 0)]
