import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree, isEqual

class TestInvertBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_invert_binary_tree_example1(self):
        root = buildTree([1,2,3,4,5,6,7])
        expected_result = buildTree([1,3,2,7,6,5,4])
        result = self.solution.invertTree(root)

        self.assertTrue(isEqual(result, expected_result))

    def test_invert_binary_tree_example2(self):
        root = buildTree([3,2,1])
        expected_result = buildTree([3,1,2])
        result = self.solution.invertTree(root)

        self.assertTrue(isEqual(result, expected_result))

    def test_invert_binary_tree_example3(self):
        root = buildTree([])
        expected_result = buildTree([])
        result = self.solution.invertTree(root)

        self.assertTrue(isEqual(result, expected_result))

if __name__ == "__main__":
    unittest.main()