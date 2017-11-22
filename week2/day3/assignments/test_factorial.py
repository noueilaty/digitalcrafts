import unittest
from factorial import Factorial

class TestFactorial(unittest.TestCase):

    def setUp(self):
        self.factorial = Factorial()

    def test_is_object(self):
        self.assertNotEqual(self.factorial, None)

    def test_factorial(self):
        self.assertEqual(120, self.factorial.factorial(5))
        self.assertEqual(0, self.factorial.factorial(0))

unittest.main()
