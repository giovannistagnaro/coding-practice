import unittest
from solution import Solution

class TestValidPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_valid_palindrome_example1(self):
        s = "A man, a plan, a canal: Panama"
        result = self.solution.isPalindrome(s)
        self.assertTrue(result)

    def test_valid_palindrome_example2(self):
        s = "race a car"
        result = self.solution.isPalindrome(s)
        self.assertFalse(result)

    def test_valid_palindrome_example3(self):
        s = " "
        result = self.solution.isPalindrome(s)
        self.assertTrue(result)

    def test_valid_palindrome_no_alnum(self):
        s = "#$*(%%&$*%(_!#%))"
        result = self.solution.isPalindrome(s)
        self.assertTrue(result)

    def test_valid_palindrome_all_nums(self):
        s = "1690746470961"
        result = self.solution.isPalindrome(s)
        self.assertTrue(result)

    def test_valid_palindrome_almost_palindrome(self):
        s = "ab5opnaPo5ba"
        result = self.solution.isPalindrome(s)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()