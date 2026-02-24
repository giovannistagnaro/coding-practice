import unittest
from solution import Solution

class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_respeating_char_replacement_example1(self):
        s, k = "XYYX", 2
        expected_result = 4
        result = self.solution.characterReplacement(s, k)

    def test_longest_respeating_char_replacement_example2(self):
        s, k = "AAABABB", 1
        expected_result = 5
        result = self.solution.characterReplacement(s, k)

    def test_longest_respeating_char_replacement_no_k(self):
        s, k = "AABABBBA", 0
        expected_result = 3
        result = self.solution.characterReplacement(s, k)

    def test_longest_respeating_char_replacement_high_k(self):
        s, k = "GIOVANNI", 8
        expected_result = 8
        result = self.solution.characterReplacement(s, k)

    def test_longest_respeating_char_replacement_all_same(self):
        s, k = "AAAAAAAAAA", 5
        expected_result = 10
        result = self.solution.characterReplacement(s, k)


if __name__ == "__main__":
    unittest.main()