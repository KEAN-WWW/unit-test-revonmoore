"""Calculator Code Assignment."""

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
    """Return a divided by b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

class Calculator:
    """Calculator class wrapping arithmetic functions as static methods."""

    @staticmethod
    def add(a: int, b: int) -> int:
        return add(a, b)

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return subtract(a, b)

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return multiply(a, b)

    @staticmethod
    def divide(a: int, b: int) -> float:
        return divide(a, b)

