"""Calculator module with arithmetic functions and a Calculator class."""

def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Return the result of a minus b."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b

def divide(a: int, b: int) -> float:
    """Return the result of a divided by b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

class Calculator:
    """Calculator class wrapping arithmetic functions as static methods."""

    @staticmethod
    def add(a: int, b: int) -> int:
        """Return the sum of a and b."""
        return add(a, b)

    @staticmethod
    def subtract(a: int, b: int) -> int:
        """Return the result of a minus b."""
        return subtract(a, b)

    @staticmethod
    def multiply(a: int, b: int) -> int:
        """Return the product of a and b."""
        return multiply(a, b)

    @staticmethod
    def divide(a: int, b: int) -> float:
        """Return the result of a divided by b. Raises ZeroDivisionError if b == 0."""
        return divide(a, b)

