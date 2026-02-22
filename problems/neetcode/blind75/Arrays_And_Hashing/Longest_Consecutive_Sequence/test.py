import unittest
from solution import Solution

class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_consecutive_sequence_example1(self):
        nums = [2,20,4,10,3,4,5]
        expected_result = 4
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(expected_result, result)

    def test_longest_consecutive_sequence_example2(self):
        nums = [0,3,2,5,4,6,1,1]
        expected_result = 7
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(expected_result, result)

    def test_longest_consecutive_sequence_blank(self):
        nums = []
        expected_result = 0
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(expected_result, result)

    def test_longest_consecutive_sequence_singles(self):
        nums = [1, 3, 5, 7, 9]
        expected_result = 1
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(expected_result, result)

    def test_longest_consecutive_sequence_all_same(self):
        nums = [1, 1, 1, 1, 1, 1]
        expected_result = 1
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(expected_result, result)

    def test_longest_consecutive_sequence_negatives(self):
        nums = [-3, -4, -2, -1, 0, 3, 2, 1]
        expected_result = 8
        result = self.solution.longestConsecutive(nums)
        self.assertEqual(expected_result, result)
    
if __name__ == "__main__":
    unittest.main()