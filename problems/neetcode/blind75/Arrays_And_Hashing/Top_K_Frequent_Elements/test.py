import unittest
from solution import Solution

class TestTopKFrequentElements(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    def test_top_k_frequent_elements_example1(self):
        nums, k = [1,2,2,3,3,3], 2
        result = self.solution.topKFrequent(nums, k)
        expected = [2, 3]

        result_set = frozenset(result)
        expected_set = frozenset(expected)
        self.assertEqual(result_set, expected_set)

    def test_top_k_frequent_elements_example2(self):
        nums, k = [7, 7], 1
        result = self.solution.topKFrequent(nums, k)
        expected = [7]

        result_set = frozenset(result)
        expected_set = frozenset(expected)
        self.assertEqual(result_set, expected_set)

    def test_top_k_frequent_elements_k_equals_nums_length(self):
        nums, k = [1, 2, 3, 4, 5, 6], 6
        result = self.solution.topKFrequent(nums, k)
        expected = [1, 2, 3, 4, 5, 6]

        result_set = frozenset(result)
        expected_set = frozenset(expected)
        self.assertEqual(result_set, expected_set)

    def test_top_k_frequent_elements_negatives(self):
        nums, k = [1, -2, 3, -4, -4, 3, 3, -2, -2, -2], 1
        result = self.solution.topKFrequent(nums, k)
        expected = [-2]

        result_set = frozenset(result)
        expected_set = frozenset(expected)
        self.assertEqual(result_set, expected_set)

if __name__ == "__main__":
    unittest.main()