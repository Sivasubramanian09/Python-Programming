import mathlib

def test_calc_total():
    total = mathlib.calc_total(4,5)
    assert total == 9
    
def test_calc_multiply():
    result = mathlib.calc_multiply(2*3)
    assert result == 6