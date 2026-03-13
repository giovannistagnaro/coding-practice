import unittest
from solution import Solution

class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_palindromic_example1(self):
        s = "ababd"
        expected_result = {"aba", "bab"}
        result = self.solution.longestPalindrome(s)

        self.assertTrue(result in expected_result)

    def test_longest_palindromic_example2(self):
        s = "abbc"
        expected_result = "bb"
        result = self.solution.longestPalindrome(s)

        self.assertEqual(result, expected_result)

    def test_longest_palindromic_single(self):
        s = "a"
        expected_result = "a"
        result = self.solution.longestPalindrome(s)

        self.assertEqual(result, expected_result)

    def test_longest_palindromic_pair(self):
        s = "bb"
        expected_result = "bb"
        result = self.solution.longestPalindrome(s)

        self.assertEqual(result, expected_result)

    def test_longest_palindromic_long_but_small_answer(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        result = self.solution.longestPalindrome(s)

        self.assertTrue(result in s)

if __name__ == "__main__":
    unittest.main()