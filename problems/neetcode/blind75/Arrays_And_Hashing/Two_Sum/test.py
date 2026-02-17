import unittest
from solution import Solution

class testTwoSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_two_sum_example1(self):
        nums = [3,4,5,6]
        target = 7
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_two_sum_example2(self):
        nums = [4,5,6]
        target = 10
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 2])

    def test_two_sum_example3(self):
        nums = [5, 5]
        target = 10
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_two_sum_negatives(self):
        nums = [1, -2, 3, -4, 5, -6, 7, -8, 9, -23]
        target = -20
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [2, 9])

    def test_two_sum_zero(self):
        nums = [0, 1, -2, 3, -4, 5, -6, 7, -8, 9, -23, 0]
        target = 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 11])

    def test_two_sum_all_same(self):
        nums = [4, 4, 4, 4, 4, 4]
        target = 8
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_two_sum_example4(self):
        nums = [2,5,5,11]
        target = 10
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [1, 2])

if __name__ == '__main__':
    unittest.main()