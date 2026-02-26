import unittest
from solution import Solution

class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_min_in_rotated_sorted_arr_example1(self):
        nums = [3,4,5,6,1,2]
        expected_result = 1
        result = self.solution.findMin(nums)

        self.assertEqual(expected_result, result)

    def test_find_min_in_rotated_sorted_arr_example2(self):
        nums = [4,5,0,1,2,3]
        expected_result = 0
        result = self.solution.findMin(nums)

        self.assertEqual(expected_result, result)

    def test_find_min_in_rotated_sorted_arr_example3(self):
        nums = [4,5,6,7]
        expected_result = 4
        result = self.solution.findMin(nums)

        self.assertEqual(expected_result, result)

    def test_find_min_in_rotated_sorted_arr_small(self):
        nums = [2, 1]
        expected_result = 1
        result = self.solution.findMin(nums)

        self.assertEqual(expected_result, result)

    def test_find_min_in_rotated_sorted_arr_smaller(self):
        nums = [4]
        expected_result = 4
        result = self.solution.findMin(nums)

        self.assertEqual(expected_result, result)

    def test_find_min_in_rotated_sorted_arr_negatives(self):
        nums = [-2,-1,-4,-3]
        expected_result = -4
        result = self.solution.findMin(nums)

        self.assertEqual(expected_result, result)

    def test_find_min_in_rotated_sorted_arr_negatives_and_positives(self):
        nums = [0,1,2,-2,-1]
        expected_result = -2
        result = self.solution.findMin(nums)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()