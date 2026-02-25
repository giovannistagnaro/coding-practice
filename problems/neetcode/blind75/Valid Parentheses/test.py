import unittest
from solution import Solution

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses_example1(self):
        s = "([{}])"
        result = self.solution.isValid(s)

        self.assertTrue(result)

    def test_valid_parentheses_example2(self):
        s = "([{}])"
        result = self.solution.isValid(s)

        self.assertTrue(result)

    def test_valid_parentheses_example3(self):
        s = "([{}])"
        result = self.solution.isValid(s)

        self.assertFalse(result)

    def test_valid_parentheses_all_opening(self):
        s = "([{"
        result = self.solution.isValid(s)

        self.assertFalse(result)

    def test_valid_parentheses_all_closing(self):
        s = "}])"
        result = self.solution.isValid(s)

        self.assertFalse(result)