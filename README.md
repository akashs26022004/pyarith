# pyarith

[![PyPI version](https://img.shields.io/pypi/v/pyarith.svg)](https://pypi.org/project/pyarith/)
[![Python versions](https://img.shields.io/pypi/pyversions/pyarith.svg)](https://pypi.org/project/pyarith/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A clean, dependency-free arithmetic utility library for Python.

---

## Feature

| Category | Functions |
|---|---|
| **Basic** | `add`, `subtract`, `multiply`, `divide` |
| **Integer ops** | `floor_divide`, `modulo` |
| **Power & roots** | `power`, `sqrt`, `nth_root` |
| **Aggregates** | `sum_all`, `product_all`, `average` |
| **Utilities** | `absolute`, `clamp` |

- ✅ **No external dependencies** — only Python's standard library
- ✅ **Typed** — full type hints on every function
- ✅ **Descriptive exceptions** — `DivisionByZeroError`, `NegativeSqrtError`, `InvalidRootError`
- ✅ **Fully documented** — NumPy-style docstrings with examples
- ✅ **Tested** — comprehensive pytest suite

---

## Installation

```bash
pip install pyarith
```

---

## Quick Start

```python
import pyarith as pa

# Basic operations
pa.add(3, 4)          # 7
pa.subtract(10, 3)    # 7
pa.multiply(6, 7)     # 42
pa.divide(10, 4)      # 2.5

# Power & roots
pa.power(2, 10)       # 1024
pa.sqrt(16)           # 4.0
pa.nth_root(27, 3)    # 3.0

# Integer operations
pa.floor_divide(7, 2) # 3
pa.modulo(10, 3)      # 1

# Aggregates
pa.sum_all(1, 2, 3, 4, 5)       # 15
pa.product_all(1, 2, 3, 4, 5)   # 120
pa.average(2, 4, 6, 8)          # 5.0

# Utilities
pa.absolute(-7)           # 7
pa.clamp(15, 0, 10)       # 10  (clamped to max)
pa.clamp(-5, 0, 10)       # 0   (clamped to min)
```

---

## Error Handling

`pyarith` uses a typed exception hierarchy so you can catch errors precisely:

```python
from pyarith.exceptions import DivisionByZeroError, NegativeSqrtError, InvalidRootError

try:
    result = pa.divide(10, 0)
except DivisionByZeroError as e:
    print(e)  # Cannot perform 'divide': divisor must not be zero.

try:
    result = pa.sqrt(-4)
except NegativeSqrtError as e:
    print(e)  # Cannot compute sqrt of negative number: -4.

try:
    result = pa.nth_root(-4, 2)  # even root of negative
except InvalidRootError as e:
    print(e)
```

All exceptions inherit from `pyarith.exceptions.PyArithError`, so you can also catch them all at once:

```python
from pyarith.exceptions import PyArithError

try:
    pa.divide(5, 0)
except PyArithError as e:
    print(f"pyarith error: {e}")
```

---

## API Reference

### `add(a, b)`
Returns `a + b`.

### `subtract(a, b)`
Returns `a - b`.

### `multiply(a, b)`
Returns `a * b`.

### `divide(a, b)` → `float`
Returns `a / b`. Raises `DivisionByZeroError` if `b == 0`.

### `floor_divide(a, b)` → `int`
Returns `a // b`. Raises `DivisionByZeroError` if `b == 0`.

### `modulo(a, b)`
Returns `a % b`. Raises `DivisionByZeroError` if `b == 0`.

### `power(base, exponent)`
Returns `base ** exponent`.

### `sqrt(x)` → `float`
Returns the non-negative square root of `x`. Raises `NegativeSqrtError` if `x < 0`.

### `nth_root(x, n)` → `float`
Returns the *n*-th real root of `x`.
- Supports negative `x` when `n` is odd.
- Raises `InvalidRootError` if `n == 0`, or if `n` is even and `x < 0`.

### `sum_all(*args)`
Returns the sum of all arguments. Raises `ValueError` if called with no args.

### `product_all(*args)`
Returns the product of all arguments. Raises `ValueError` if called with no args.

### `average(*args)` → `float`
Returns the arithmetic mean. Raises `ValueError` if called with no args.

### `absolute(x)`
Returns `abs(x)`.

### `clamp(value, minimum, maximum)`
Returns `value` clamped to `[minimum, maximum]`. Raises `ValueError` if `minimum > maximum`.

---

## Development

```bash
# Clone and install in editable mode with dev extras
git clone https://github.com/akashs/pyarith.git
cd pyarith
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=pyarith --cov-report=term-missing
```

---

## Publishing to PyPI

```bash
# 1. Build the distribution packages
python -m build

# 2. Upload to TestPyPI first (recommended)
twine upload --repository testpypi dist/*

# 3. Verify the TestPyPI install works
pip install --index-url https://test.pypi.org/simple/ pyarith

# 4. Upload to PyPI
twine upload dist/*
```

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

---

## License

MIT © Akash S
