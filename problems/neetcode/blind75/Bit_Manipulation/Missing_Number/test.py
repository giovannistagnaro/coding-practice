import unittest
from solution import Solution

class TestMissingNumber(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_missing_number_example1(self):
        nums = [1,2,3]
        expected_result = 0
        result = self.solution.missingNumber(nums)
        self.assertEqual(expected_result, result)

    def test_missing_number_example2(self):
        nums = [0,2]
        expected_result = 1
        result = self.solution.missingNumber(nums)
        self.assertEqual(expected_result, result)

    def test_missing_number_missing_n(self):
        nums = [0,1,2,3]
        expected_result = 4
        result = self.solution.missingNumber(nums)
        self.assertEqual(expected_result, result)

    def test_missing_number_min(self):
        nums = [0]
        expected_result = 1
        result = self.solution.missingNumber(nums)
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()