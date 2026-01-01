import unittest
from solution import Solution

class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_two_sum_example1(self):
        nums = [2,7,11,15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0,1])

    def test_two_sum_example2(self):
        nums = [3,2,4]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [1,2])

    def test_two_sum_example3(self):
        nums = [3,3]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0,1])

    def test_two_sum_zeroes(self):
        result = self.solution.twoSum([0, 0, 0, 0], 0)
        self.assertEqual(result, [0, 1])

    def test_two_sum_large_numbers(self):
        result = self.solution.twoSum([1000000, 2000000], 3000000)
        self.assertEqual(result, [0, 1])

    def test_two_sum_first_and_last(self):
        result = self.solution.twoSum([1, 2, 2, 4], 5)
        self.assertEqual(result, [0, 3]) 

    def test_two_sum_no_solution(self):
        result = self.solution.twoSum([1, 2, 3], 10)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()