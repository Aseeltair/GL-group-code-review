"""
sum_positive_numbers.py

This module provides a function to sum only the positive numbers in a list.
"""

from typing import List


def sum_positive_numbers(numbers: List[float]) -> float:
    """
    Calculate the sum of positive numbers in a given list.

    Args:
        numbers (List[float]): A list of floating point or integer numbers.

    Returns:
        float: The sum of all positive numbers in the list. If no positive numbers, returns 0.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If any element in the list is not a number.

    Examples:
        >>> sum_positive_numbers([1, -2, 3.5, 0, -1])
        4.5
        >>> sum_positive_numbers([-10, -20, -30])
        0
        >>> sum_positive_numbers([5, 10, 15])
        30
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements in the list must be numbers.")

    return sum(num for num in numbers if num > 0)
