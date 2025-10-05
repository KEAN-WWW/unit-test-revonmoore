"""Tests for divide function in calculator.py."""

import pytest
from app.calculator import divide

def test_division_valid():
    """Check normal division works."""
    assert divide(10, 2) == 5.0
    assert divide(-9, 3) == -3.0

def test_division_by_zero():
    """Check division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
