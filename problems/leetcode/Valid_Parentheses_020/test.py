import unittest
from solution import Solution

class TestValidPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses_example1(self):
        s = "()"
        result = self.solution.isValid(s)
        self.assertTrue(result)

    def test_valid_parentheses_example2(self):
        s = "()[]{}"
        result = self.solution.isValid(s)
        self.assertTrue(result)

    def test_valid_palindrome_example3(self):
        s = "(]"
        result = self.solution.isValid(s)
        self.assertFalse(result)

    def test_valid_palindrome_example4(self):
        s = "([])"
        result = self.solution.isValid(s)
        self.assertTrue(result)

    def test_valid_palindrome_example5(self):
        s = "([)]"
        result = self.solution.isValid(s)
        self.assertFalse(result)

    def test_valid_parentheses_empty(self):
        s = ""
        result = self.solution.isValid(s)
        self.assertTrue(result)

    def test_valid_parentheses_long_valid(self):
        s = "([{}])()[]{}[({})]{}()[]{}[({})]{}()[]{}"
        result = self.solution.isValid(s)
        self.assertTrue(result)

    def test_valid_parentheses_deep_mismatch(self):
        s = "((({})))({[}])"
        result = self.solution.isValid(s)
        self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()