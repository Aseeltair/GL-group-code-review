"""
multiply.py

This module provides a function to multiply two numbers.
"""

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the result.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.

    Raises:
        TypeError: If the inputs are not numbers.

    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(5.5, 2)
        11.0
        >>> multiply(-4, 3)
        -12
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")

    return a * b
