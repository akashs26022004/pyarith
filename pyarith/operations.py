"""
Core arithmetic operations for the pyarith package.

All functions accept int or float values and raise typed exceptions
(defined in pyarith.exceptions) instead of raw Python errors so that
callers can handle errors without string-matching.

Type aliases
------------
Number = int | float
"""

from __future__ import annotations

import math
from typing import Iterable, Union

from .exceptions import (
    DivisionByZeroError,
    InvalidRootError,
    NegativeSqrtError,
)

Number = Union[int, float]


# ---------------------------------------------------------------------------
# Basic operations
# ---------------------------------------------------------------------------


def add(a: Number, b: Number) -> Number:
    """Return the sum of *a* and *b*.

    Parameters
    ----------
    a, b : int or float
        The operands.

    Returns
    -------
    int or float
        ``a + b``

    Examples
    --------
    >>> add(3, 4)
    7
    >>> add(1.5, 2.5)
    4.0
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference *a* minus *b*.

    Parameters
    ----------
    a, b : int or float

    Returns
    -------
    int or float
        ``a - b``

    Examples
    --------
    >>> subtract(10, 3)
    7
    >>> subtract(0.5, 1.5)
    -1.0
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of *a* and *b*.

    Parameters
    ----------
    a, b : int or float

    Returns
    -------
    int or float
        ``a * b``

    Examples
    --------
    >>> multiply(6, 7)
    42
    >>> multiply(2.5, 4)
    10.0
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return *a* divided by *b* (true division).

    Parameters
    ----------
    a : int or float
        Dividend.
    b : int or float
        Divisor (must not be zero).

    Returns
    -------
    float

    Raises
    ------
    DivisionByZeroError
        If *b* is zero.

    Examples
    --------
    >>> divide(10, 4)
    2.5
    >>> divide(-9, 3)
    -3.0
    """
    if b == 0:
        raise DivisionByZeroError("divide")
    return a / b


# ---------------------------------------------------------------------------
# Integer-style operations
# ---------------------------------------------------------------------------


def floor_divide(a: Number, b: Number) -> int:
    """Return *a* floor-divided by *b* (integer division).

    The result is always rounded toward negative infinity, matching
    Python's ``//`` operator semantics.

    Parameters
    ----------
    a : int or float
    b : int or float
        Must not be zero.

    Returns
    -------
    int

    Raises
    ------
    DivisionByZeroError
        If *b* is zero.

    Examples
    --------
    >>> floor_divide(7, 2)
    3
    >>> floor_divide(-7, 2)
    -4
    """
    if b == 0:
        raise DivisionByZeroError("floor_divide")
    return int(a // b)


def modulo(a: Number, b: Number) -> Number:
    """Return the remainder of *a* divided by *b*.

    Parameters
    ----------
    a : int or float
    b : int or float
        Must not be zero.

    Returns
    -------
    int or float

    Raises
    ------
    DivisionByZeroError
        If *b* is zero.

    Examples
    --------
    >>> modulo(10, 3)
    1
    >>> modulo(10.5, 3)
    1.5
    """
    if b == 0:
        raise DivisionByZeroError("modulo")
    return a % b


# ---------------------------------------------------------------------------
# Power & roots
# ---------------------------------------------------------------------------


def power(base: Number, exponent: Number) -> Number:
    """Raise *base* to the power of *exponent*.

    Parameters
    ----------
    base : int or float
    exponent : int or float

    Returns
    -------
    int or float

    Examples
    --------
    >>> power(2, 10)
    1024
    >>> power(9, 0.5)
    3.0
    """
    return base ** exponent


def sqrt(x: Number) -> float:
    """Return the non-negative square root of *x*.

    Parameters
    ----------
    x : int or float
        Must be >= 0.

    Returns
    -------
    float

    Raises
    ------
    NegativeSqrtError
        If *x* is negative.

    Examples
    --------
    >>> sqrt(16)
    4.0
    >>> sqrt(2)
    1.4142135623730951
    """
    if x < 0:
        raise NegativeSqrtError(x)
    return math.sqrt(x)


def nth_root(x: Number, n: int) -> float:
    """Return the *n*-th real root of *x*.

    For odd *n*, negative *x* values are supported (the result is negative).
    For even *n*, *x* must be >= 0.

    Parameters
    ----------
    x : int or float
        The radicand.
    n : int
        The degree of the root (must be != 0).

    Returns
    -------
    float

    Raises
    ------
    InvalidRootError
        If *n* is 0, or if *n* is even and *x* is negative.

    Examples
    --------
    >>> nth_root(27, 3)
    3.0
    >>> nth_root(-8, 3)
    -2.0
    >>> nth_root(16, 4)
    2.0
    """
    if n == 0:
        raise InvalidRootError("The root degree 'n' must not be zero.")
    if x < 0:
        if n % 2 == 0:
            raise InvalidRootError(
                f"Cannot compute even root (n={n}) of a negative number ({x})."
            )
        # Odd root of negative: compute on positive then negate
        return -((-x) ** (1 / n))
    return x ** (1 / n)


# ---------------------------------------------------------------------------
# Aggregates
# ---------------------------------------------------------------------------


def sum_all(*args: Number) -> Number:
    """Return the sum of all provided numbers.

    Parameters
    ----------
    *args : int or float
        One or more numbers.

    Returns
    -------
    int or float

    Raises
    ------
    ValueError
        If no arguments are provided.

    Examples
    --------
    >>> sum_all(1, 2, 3, 4, 5)
    15
    >>> sum_all(1.1, 2.2, 3.3)
    6.6000000000000005
    """
    if not args:
        raise ValueError("sum_all requires at least one argument.")
    return sum(args)


def product_all(*args: Number) -> Number:
    """Return the product of all provided numbers.

    Parameters
    ----------
    *args : int or float
        One or more numbers.

    Returns
    -------
    int or float

    Raises
    ------
    ValueError
        If no arguments are provided.

    Examples
    --------
    >>> product_all(1, 2, 3, 4, 5)
    120
    >>> product_all(2, 3.5)
    7.0
    """
    if not args:
        raise ValueError("product_all requires at least one argument.")
    result: Number = 1
    for n in args:
        result = result * n
    return result


def average(*args: Number) -> float:
    """Return the arithmetic mean of the provided numbers.

    Parameters
    ----------
    *args : int or float
        One or more numbers.

    Returns
    -------
    float

    Raises
    ------
    ValueError
        If no arguments are provided.

    Examples
    --------
    >>> average(2, 4, 6, 8)
    5.0
    >>> average(100)
    100.0
    """
    if not args:
        raise ValueError("average requires at least one argument.")
    return sum(args) / len(args)


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------


def absolute(x: Number) -> Number:
    """Return the absolute value of *x*.

    Parameters
    ----------
    x : int or float

    Returns
    -------
    int or float

    Examples
    --------
    >>> absolute(-7)
    7
    >>> absolute(3.14)
    3.14
    """
    return abs(x)


def clamp(value: Number, minimum: Number, maximum: Number) -> Number:
    """Clamp *value* so it lies in the closed interval [*minimum*, *maximum*].

    Parameters
    ----------
    value : int or float
        The input value.
    minimum : int or float
        Lower bound (inclusive).
    maximum : int or float
        Upper bound (inclusive).

    Returns
    -------
    int or float

    Raises
    ------
    ValueError
        If *minimum* > *maximum*.

    Examples
    --------
    >>> clamp(15, 0, 10)
    10
    >>> clamp(-5, 0, 10)
    0
    >>> clamp(7, 0, 10)
    7
    """
    if minimum > maximum:
        raise ValueError(
            f"'minimum' ({minimum}) must not be greater than 'maximum' ({maximum})."
        )
    return max(minimum, min(value, maximum))
