import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree, isEqual

class TestKthSmallestIntegerInBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kth_smallest_example1(self):
        root = buildTree([2,1,3])
        k = 1
        expected_result = 1
        result = self.solution.kthSmallest(root, k)

        self.assertEqual(expected_result, result)

    def test_kth_smallest_example2(self):
        root = buildTree([4,3,5,2,None])
        k = 4
        expected_result = 5
        result = self.solution.kthSmallest(root, k)

        self.assertEqual(expected_result, result)

    def test_kth_smallest_single(self):
        root = buildTree([4])
        k = 1
        expected_result = 4
        result = self.solution.kthSmallest(root, k)

        self.assertEqual(expected_result, result)   

    def test_kth_smallest_all_right(self):
        root = buildTree([4,None,5,None,6,None,7])
        k = 3
        expected_result = 6
        result = self.solution.kthSmallest(root, k)

        self.assertEqual(expected_result, result)  

    def test_kth_smallest_all_left(self):
        root = buildTree([4,3,None,2,None,1])
        k = 2
        expected_result = 2
        result = self.solution.kthSmallest(root, k)

        self.assertEqual(expected_result, result)  

if __name__ == "__main__":
    unittest.main()