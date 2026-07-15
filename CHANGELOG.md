# Changelog

All notable changes to **pyarith** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] — 2026-07-15

### Added
- `add(a, b)` — addition
- `subtract(a, b)` — subtraction
- `multiply(a, b)` — multiplication
- `divide(a, b)` — true division with `DivisionByZeroError`
- `floor_divide(a, b)` — integer (floor) division
- `modulo(a, b)` — remainder operation
- `power(base, exponent)` — exponentiation
- `sqrt(x)` — square root with `NegativeSqrtError`
- `nth_root(x, n)` — n-th real root with `InvalidRootError`
- `sum_all(*args)` — sum of arbitrary number of values
- `product_all(*args)` — product of arbitrary number of values
- `average(*args)` — arithmetic mean
- `absolute(x)` — absolute value
- `clamp(value, minimum, maximum)` — range clamping
- Custom exception hierarchy: `PyArithError`, `DivisionByZeroError`, `NegativeSqrtError`, `InvalidRootError`
- Full type annotations
- NumPy-style docstrings with examples
- pytest test suite (100 % function coverage)
- `pyproject.toml` build configuration (PEP 517/518)
