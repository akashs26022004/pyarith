"""
Unit tests for pyarith.

Run with:
    python -m pytest tests/ -v
"""

import pytest

from pyarith import (
    absolute,
    add,
    average,
    clamp,
    divide,
    floor_divide,
    modulo,
    multiply,
    nth_root,
    power,
    product_all,
    sqrt,
    subtract,
    sum_all,
)
from pyarith.exceptions import (
    DivisionByZeroError,
    InvalidRootError,
    NegativeSqrtError,
)


# ---------------------------------------------------------------------------
# add
# ---------------------------------------------------------------------------
class TestAdd:
    def test_integers(self):
        assert add(3, 4) == 7

    def test_floats(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)

    def test_negative(self):
        assert add(-1, -2) == -3

    def test_zero(self):
        assert add(0, 0) == 0

    def test_mixed(self):
        assert add(1, 2.0) == pytest.approx(3.0)


# ---------------------------------------------------------------------------
# subtract
# ---------------------------------------------------------------------------
class TestSubtract:
    def test_integers(self):
        assert subtract(10, 3) == 7

    def test_floats(self):
        assert subtract(0.5, 1.5) == pytest.approx(-1.0)

    def test_negative_result(self):
        assert subtract(1, 5) == -4


# ---------------------------------------------------------------------------
# multiply
# ---------------------------------------------------------------------------
class TestMultiply:
    def test_integers(self):
        assert multiply(6, 7) == 42

    def test_floats(self):
        assert multiply(2.5, 4) == pytest.approx(10.0)

    def test_by_zero(self):
        assert multiply(99, 0) == 0

    def test_negatives(self):
        assert multiply(-3, -4) == 12


# ---------------------------------------------------------------------------
# divide
# ---------------------------------------------------------------------------
class TestDivide:
    def test_exact(self):
        assert divide(10, 2) == pytest.approx(5.0)

    def test_fractional(self):
        assert divide(10, 4) == pytest.approx(2.5)

    def test_negative(self):
        assert divide(-9, 3) == pytest.approx(-3.0)

    def test_division_by_zero_raises(self):
        with pytest.raises(DivisionByZeroError):
            divide(5, 0)


# ---------------------------------------------------------------------------
# floor_divide
# ---------------------------------------------------------------------------
class TestFloorDivide:
    def test_positive(self):
        assert floor_divide(7, 2) == 3

    def test_negative(self):
        assert floor_divide(-7, 2) == -4

    def test_zero_raises(self):
        with pytest.raises(DivisionByZeroError):
            floor_divide(10, 0)


# ---------------------------------------------------------------------------
# modulo
# ---------------------------------------------------------------------------
class TestModulo:
    def test_integers(self):
        assert modulo(10, 3) == 1

    def test_floats(self):
        assert modulo(10.5, 3) == pytest.approx(1.5)

    def test_zero_raises(self):
        with pytest.raises(DivisionByZeroError):
            modulo(5, 0)


# ---------------------------------------------------------------------------
# power
# ---------------------------------------------------------------------------
class TestPower:
    def test_integer_exponent(self):
        assert power(2, 10) == 1024

    def test_fractional_exponent(self):
        assert power(9, 0.5) == pytest.approx(3.0)

    def test_zero_exponent(self):
        assert power(100, 0) == 1

    def test_negative_base(self):
        assert power(-2, 3) == -8


# ---------------------------------------------------------------------------
# sqrt
# ---------------------------------------------------------------------------
class TestSqrt:
    def test_perfect_square(self):
        assert sqrt(16) == pytest.approx(4.0)

    def test_non_perfect(self):
        assert sqrt(2) == pytest.approx(1.4142135623730951)

    def test_zero(self):
        assert sqrt(0) == pytest.approx(0.0)

    def test_negative_raises(self):
        with pytest.raises(NegativeSqrtError):
            sqrt(-1)


# ---------------------------------------------------------------------------
# nth_root
# ---------------------------------------------------------------------------
class TestNthRoot:
    def test_cube_root(self):
        assert nth_root(27, 3) == pytest.approx(3.0)

    def test_negative_cube_root(self):
        assert nth_root(-8, 3) == pytest.approx(-2.0)

    def test_fourth_root(self):
        assert nth_root(16, 4) == pytest.approx(2.0)

    def test_zero_n_raises(self):
        with pytest.raises(InvalidRootError):
            nth_root(8, 0)

    def test_even_root_of_negative_raises(self):
        with pytest.raises(InvalidRootError):
            nth_root(-4, 2)


# ---------------------------------------------------------------------------
# sum_all
# ---------------------------------------------------------------------------
class TestSumAll:
    def test_integers(self):
        assert sum_all(1, 2, 3, 4, 5) == 15

    def test_single(self):
        assert sum_all(42) == 42

    def test_floats(self):
        assert sum_all(1.0, 2.0) == pytest.approx(3.0)

    def test_no_args_raises(self):
        with pytest.raises(ValueError):
            sum_all()


# ---------------------------------------------------------------------------
# product_all
# ---------------------------------------------------------------------------
class TestProductAll:
    def test_integers(self):
        assert product_all(1, 2, 3, 4, 5) == 120

    def test_single(self):
        assert product_all(7) == 7

    def test_no_args_raises(self):
        with pytest.raises(ValueError):
            product_all()


# ---------------------------------------------------------------------------
# average
# ---------------------------------------------------------------------------
class TestAverage:
    def test_even_numbers(self):
        assert average(2, 4, 6, 8) == pytest.approx(5.0)

    def test_single(self):
        assert average(100) == pytest.approx(100.0)

    def test_no_args_raises(self):
        with pytest.raises(ValueError):
            average()


# ---------------------------------------------------------------------------
# absolute
# ---------------------------------------------------------------------------
class TestAbsolute:
    def test_negative(self):
        assert absolute(-7) == 7

    def test_positive(self):
        assert absolute(3.14) == pytest.approx(3.14)

    def test_zero(self):
        assert absolute(0) == 0


# ---------------------------------------------------------------------------
# clamp
# ---------------------------------------------------------------------------
class TestClamp:
    def test_above_max(self):
        assert clamp(15, 0, 10) == 10

    def test_below_min(self):
        assert clamp(-5, 0, 10) == 0

    def test_within_range(self):
        assert clamp(7, 0, 10) == 7

    def test_invalid_range_raises(self):
        with pytest.raises(ValueError):
            clamp(5, 10, 0)
