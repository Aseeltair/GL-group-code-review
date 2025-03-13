"""
test_sum_positive_numbers.py

Unit tests for the sum_positive_numbers function.
"""

import unittest
from solutions.sum_positive_numbers import sum_positive_numbers


class TestSumPositiveNumbers(unittest.TestCase):
    """Tests for sum_positive_numbers function."""

    def test_positive_numbers(self):
        """Should return the sum of positive numbers."""
        self.assertEqual(sum_positive_numbers([1, 2, 3]), 6)

    def test_mixed_numbers(self):
        """Should sum only positive numbers and ignore negatives."""
        self.assertEqual(sum_positive_numbers([1, -2, 3.5, 0, -1]), 4.5)

    def test_all_negative_numbers(self):
        """Should return 0 if there are no positive numbers."""
        self.assertEqual(sum_positive_numbers([-10, -20, -30]), 0)

    def test_empty_list(self):
        """Should return 0 for an empty list."""
        self.assertEqual(sum_positive_numbers([]), 0)

    def test_invalid_input_type(self):
        """Should raise TypeError for non-list input."""
        with self.assertRaises(TypeError):
            sum_positive_numbers("invalid")

    def test_non_numeric_elements(self):
        """Should raise ValueError if list contains non-numeric elements."""
        with self.assertRaises(ValueError):
            sum_positive_numbers([1, 2, "three"])

if __name__ == "__main__":
    unittest.main()
