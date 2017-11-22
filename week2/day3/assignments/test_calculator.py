# Unit Testing

# What is a test?

# Agile:
# Scrim, Scrum, Unit Testing, Pair Coding, Code Reviews,


# Two approaches to Unit Testing:
# 1. Write code first then write the unit test.
# 2. Write test first then write the code. (TDD: Test Driven Development)

# Red --> Green --> Refactor --> (restart: Red)

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_can_create_calculator_object(self):
        self.assertNotEqual(self.calculator, None)

    def test_add(self):
        self.assertEqual(6, self.calculator.add(4, 2))
        self.assertEqual(0, self.calculator.add(-5, 5))
        self.assertEqual(-5, self.calculator.add(-3, -2))

    def test_subtract(self):
        self.assertEqual(3, self.calculator.subtract(9, 6))
        self.assertEqual(-3, self.calculator.subtract(-1, 2))
        self.assertEqual(-3, self.calculator.subtract(-5, -2))

    def test_multiply(self):
        self.assertEqual(10, self.calculator.multiply(2, 5))
        self.assertEqual(-3, self.calculator.multiply(-1, 3))
        self.assertEqual(6, self.calculator.multiply(-3, -2))

    def test_divide(self):
        self.assertEqual(5, self.calculator.divide(25, 5))
        self.assertEqual(-2, self.calculator.divide(-6, 3))
        self.assertEqual(3, self.calculator.divide(-9, -3))

unittest.main()
