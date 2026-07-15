"""Custom exceptions for the pyarith package."""


class PyArithError(Exception):
    """Base exception for all pyarith errors."""


class DivisionByZeroError(PyArithError):
    """Raised when a division or modulo operation is attempted with a zero divisor."""

    def __init__(self, operation: str = "divide") -> None:
        super().__init__(
            f"Cannot perform '{operation}': divisor must not be zero."
        )


class NegativeSqrtError(PyArithError):
    """Raised when sqrt is called on a negative number (real domain)."""

    def __init__(self, value: float) -> None:
        super().__init__(
            f"Cannot compute sqrt of negative number: {value}. "
            "Use a complex-aware library for imaginary results."
        )


class InvalidRootError(PyArithError):
    """Raised for invalid nth_root arguments (e.g. n=0, or even root of negative)."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
