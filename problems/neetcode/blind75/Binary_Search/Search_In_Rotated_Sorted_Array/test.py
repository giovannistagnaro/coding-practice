import unittest
from solution import Solution

class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search_in_rotated_sorted_array_example1(self):
        nums = [3,4,5,6,1,2]
        target = 1
        expected_result = 4
        result = self.solution.search(nums, target)
        
        self.assertEqual(expected_result, result)

    def test_search_in_rotated_sorted_array_example2(self):
        nums = [3,5,6,0,1,2]
        target = 4
        expected_result = -1
        result = self.solution.search(nums, target)
        
        self.assertEqual(expected_result, result)

    def test_search_in_rotated_sorted_array_left(self):
        nums = [0,1,2,3,4,5]
        target = 0
        expected_result = 0
        result = self.solution.search(nums, target)
        
        self.assertEqual(expected_result, result)

    def test_search_in_rotated_sorted_array_right(self):
        nums = [0,1,2,3,4,5]
        target = 5
        expected_result = 5
        result = self.solution.search(nums, target)
        
        self.assertEqual(expected_result, result)

    def test_search_in_rotated_sorted_array_negatives(self):
        nums = [0,1,2,3,4,-3,-2,-1]
        target = -3
        expected_result = 5
        result = self.solution.search(nums, target)
        
        self.assertEqual(expected_result, result)

    def test_search_in_rotated_sorted_array_negatives_missing(self):
        nums = [0,1,2,3,4,-3,-2,-1]
        target = -9
        expected_result = -1
        result = self.solution.search(nums, target)
        
        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()