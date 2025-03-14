"""
test_multiply.py

Unit tests for the multiply function.
"""

import unittest
from solutions.multiply import multiply


class TestMultiply(unittest.TestCase):
    """Tests for multiply function."""

    def test_positive_numbers(self):
        """Should return the product of two positive numbers."""
        self.assertEqual(multiply(2, 3), 6)

    def test_negative_numbers(self):
        """Should return the correct product for negative numbers."""
        self.assertEqual(multiply(-4, 3), -12)
        self.assertEqual(multiply(-2, -5), 10)

    def test_zero(self):
        """Should return 0 if either number is 0."""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(3, 0), 0)

    def test_floats(self):
        """Should correctly multiply floating point numbers."""
        self.assertEqual(multiply(2.5, 2), 5.0)

    def test_invalid_input_type(self):
        """Should raise TypeError if inputs are not numbers."""
        with self.assertRaises(TypeError):
            multiply("2", 3)
        with self.assertRaises(TypeError):
            multiply(2, [3])


if __name__ == "__main__":
    unittest.main()
