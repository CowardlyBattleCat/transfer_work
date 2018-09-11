
from functions import(
    f,
    sum_whole_numbers,
    sign,
    is_larger_than,
    sum_whole_numbers_descend,
    factorial,
    divisor,
    )

def test_f():
    assert f(6) == 7
    assert f(-1) == 0
    assert f(41) == 42

def test_sum_whole_numbers():
    assert sum_whole_numbers(0) == 0
    assert sum_whole_numbers(-4) == 0
    assert sum_whole_numbers(6) == 21

def test_sign():
    assert sign(6) == 1
    assert sign(-6) == -1
    assert sign(0) == 0

def test_is_larger_than():
    assert is_larger_than(3, 4) == False
    assert is_larger_than(-2, -2) == False
    assert is_larger_than(4, 3) == True

def test_sum_whole_numbers_descend():
    assert sum_whole_numbers_descend(0) == 0
    assert sum_whole_numbers_descend(-4) == 0
    assert sum_whole_numbers_descend(6) == 21

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(1.1) == TypeError('factorials of non-integer numbers are beyond the scope of this function')
    assert factorial(-2) == ValueError('factorial is not defined for negative integers')

def test_divisor():
    assert divisor(0) == 'every integer'
    assert divisor(90) == [90, 45, 30, 18, 15, 10, 9, 6, 5, 3, 2, 1, -1, -2, -3, -5, -6, -9, -10, -15, -18, -30, -45, -90]
    assert divisor(-30) == [30, 15, 10, 6, 5, 3, 2, 1, -1, -2, -3, -5, -6, -10, -15, -30]
