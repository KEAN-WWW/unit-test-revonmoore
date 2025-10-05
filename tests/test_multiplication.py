"""Unit tests for the multiply function in calculator."""

from app.calculator import multiply

def test_multiplication():
    """Test multiplication cases."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
