import unittest
from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):

    def setUp(self):
        self.palindrome = Palindrome()

    def test_create_calculator_object(self):
        self.assertNotEqual(self.palindrome, None)

    def test_reverses_input(self):
        self.assertEqual('drow', self.palindrome.reverse('word'))
        self.assertEqual('rac ecar', self.palindrome.reverse('race car'))

unittest.main()
