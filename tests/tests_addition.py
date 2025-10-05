"""Unit tests for the add function in calculator."""

from app.calculator import add

def test_addition():
    """Test addition cases."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
