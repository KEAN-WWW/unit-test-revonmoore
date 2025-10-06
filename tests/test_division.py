"""Unit tests for the divide function in calculator.py."""

import pytest
from app.calculator import divide


def test_division_valid():
    """Check that normal division works correctly."""
    assert divide(10, 2) == 5.0
    assert divide(-9, 3) == -3.0


def test_division_by_zero():
    """Check that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
