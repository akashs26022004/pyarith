"""
pyarith — A clean, dependency-free arithmetic utility library.

Provides safe, well-documented functions for:
  - Basic operations: add, subtract, multiply, divide
  - Power & roots: power, sqrt, nth_root
  - Integer ops: floor_divide, modulo
  - Aggregates: sum_all, product_all, average
  - Clamp & abs: absolute, clamp
"""

from .operations import (
    add,
    subtract,
    multiply,
    divide,
    floor_divide,
    modulo,
    power,
    sqrt,
    nth_root,
    absolute,
    clamp,
    sum_all,
    product_all,
    average,
)

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "floor_divide",
    "modulo",
    "power",
    "sqrt",
    "nth_root",
    "absolute",
    "clamp",
    "sum_all",
    "product_all",
    "average",
]

__version__ = "0.1.0"
__author__ = "Akash S"
__license__ = "MIT"
