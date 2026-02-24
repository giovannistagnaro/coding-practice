import unittest
from solution import Solution

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_sub_without_repeating_chars_example1(self):
        s = "zxyzxyz"
        expected_result = 3
        result = self.solution.lengthOfLongestSubstring(s)

        self.assertEqual(expected_result, result)

    def test_longest_sub_without_repeating_chars_example2(self):
        s = "xxxx"
        expected_result = 1
        result = self.solution.lengthOfLongestSubstring(s)

        self.assertEqual(expected_result, result)

    def test_longest_sub_without_repeating_chars_empty_string(self):
        s = ""
        expected_result = 0
        result = self.solution.lengthOfLongestSubstring(s)

        self.assertEqual(expected_result, result)

    def test_longest_sub_without_repeating_chars_whole_string(self):
        s = "abcdefg"
        expected_result = 7
        result = self.solution.lengthOfLongestSubstring(s)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()