import unittest
from solution import Solution

class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_palindrome_example1(self):
        s = "Was it a car or a cat I saw?"
        result = self.solution.isPalindrome(s)
        self.assertTrue(result)
    
    def test_valid_palindrome_example2(self):
        s = "tab a cat"
        result = self.solution.isPalindrome(s)
        self.assertFalse(result)

    def test_valid_palindrome_no_alnums(self):
        s = "%($%$%&#)#$%(@)_"
        result = self.solution.isPalindrome(s)
        self.assertTrue(result)
    
    def test_valid_palindrome_single(self):
        s = "t"
        result = self.solution.isPalindrome(s)
        self.assertTrue(result)

    def test_valid_palindrome_numbers(self):
        s = "cab5 5bac"
        result = self.solution.isPalindrome(s)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()