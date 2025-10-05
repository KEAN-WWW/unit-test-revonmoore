"""Unit tests for the divide function in calculator."""

import pytest
from app.calculator import divide

def test_division():
    """Test normal division case."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_zero_exception():
    """Test that dividing by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

