"""Unit tests for calculator functions and Calculator Assignment."""

import pytest
from app.calculator import add, subtract, multiply, divide, Calculator

def test_add():
    """Test addition with positive and negative numbers."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    """Test subtraction with positive and negative numbers."""
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3

def test_multiply():
    """Test multiplication with positive and negative numbers."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    """Test division including ZeroDivisionError handling."""
    assert divide(10, 2) == 5.0
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_calculator_class():
    """Test that Calculator class methods call the functions correctly."""
    assert Calculator.add(7, 2) == 9
    assert Calculator.subtract(7, 10) == -3
    assert Calculator.multiply(-2, -4) == 8
    assert Calculator.divide(8, 2) == 4.0

