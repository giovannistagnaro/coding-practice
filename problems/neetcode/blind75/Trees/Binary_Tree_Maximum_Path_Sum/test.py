import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree, isEqual

class TestBinaryTreeMaxPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_bin_tree_max_path_example1(self):
        root = buildTree([1,2,3])
        expected_result = 6
        result = self.solution.maxPathSum(root)

        self.assertEqual(expected_result, result)

    def test_bin_tree_max_path_example2(self):
        root = buildTree([-15,10,20,None,None,15,5,-5])
        expected_result = 40
        result = self.solution.maxPathSum(root)

        self.assertEqual(expected_result, result)

    def test_bin_tree_max_path_single(self):
        root = buildTree([-15])
        expected_result = -15
        result = self.solution.maxPathSum(root)

        self.assertEqual(expected_result, result)


    def test_bin_tree_max_path_all_negative(self):
        root = buildTree([-15,-10,-20,None,None,-15,-5,-5])
        expected_result = -5
        result = self.solution.maxPathSum(root)

        self.assertEqual(expected_result, result)

    def test_bin_tree_max_path_small_tree(self):
        print("Small tree test")
        root = buildTree([1,2])
        expected_result = 3
        result = self.solution.maxPathSum(root)

        self.assertEqual(expected_result, result)

if __name__ == "__main__":
    unittest.main()