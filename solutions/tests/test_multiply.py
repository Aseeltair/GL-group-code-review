"""
test_multiply.py

Simple test cases for the multiply function using assert statements.
"""
from solutions.multiply import multiply

# Test positive numbers
try:
    assert multiply(2, 3) == 6
    print("Test Passed: multiply(2, 3) == 6")
except AssertionError:
    print("Test Failed: multiply(2, 3) should return 6")

# Test negative numbers
try:
    assert multiply(-4, 3) == -12
    print("Test Passed: multiply(-4, 3) == -12")
except AssertionError:
    print("Test Failed: multiply(-4, 3) should return -12")

try:
    assert multiply(-2, -5) == 10
    print("Test Passed: multiply(-2, -5) == 10")
except AssertionError:
    print("Test Failed: multiply(-2, -5) should return 10")

# Test zero
try:
    assert multiply(0, 5) == 0
    print("Test Passed: multiply(0, 5) == 0")
except AssertionError:
    print("Test Failed: multiply(0, 5) should return 0")

try:
    assert multiply(3, 0) == 0
    print("Test Passed: multiply(3, 0) == 0")
except AssertionError:
    print("Test Failed: multiply(3, 0) should return 0")

# Test decimal numbers
try:
    assert multiply(2.5, 2) == 5.0
    print("Test Passed: multiply(2.5, 2) == 5.0")
except AssertionError:
    print("Test Failed: multiply(2.5, 2) should return 5.0")

# Test incorrect input
try:
    multiply("2", 3)
    print("Test Failed: multiply('2', 3) should raise TypeError")
except TypeError:
    print("Test Passed: multiply('2', 3) raised TypeError as expected")

try:
    multiply(2, [3])
    print("Test Failed: multiply(2, [3]) should raise TypeError")
except TypeError:
    print("Test Passed: multiply(2, [3]) raised TypeError as expected")

print("All assert tests executed.")
