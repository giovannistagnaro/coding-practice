import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree, isEqual

class TestMaximumDepthOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_depth_bin_tree_example1(self):
        root = buildTree([1,2,3,None,None,4])
        expected_result = 3
        result = self.solution.maxDepth(root)

        self.assertEqual(expected_result, result)

    def test_max_depth_bin_tree_example2(self):
        root = buildTree([])
        expected_result = 0
        result = self.solution.maxDepth(root)

        self.assertEqual(expected_result, result)

    def test_max_depth_bin_tree_single(self):
        root = buildTree([1])
        expected_result = 1
        result = self.solution.maxDepth(root)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()