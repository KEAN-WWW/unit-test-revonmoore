"""Unit tests for the subtract function in calculator."""

from app.calculator import subtract

def test_subtraction():
    """Test subtraction cases."""
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3
