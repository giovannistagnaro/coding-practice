import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree, isEqual

class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_level_order_example1(self):
        root = buildTree([1,2,3,4,5,6,7])
        expected_output = [[1],[2,3],[4,5,6,7]]
        result = self.solution.levelOrder(root)

        self.assertEqual(expected_output, result)

    def test_level_order_example2(self):
        root = buildTree([1])
        expected_output = [[1]]
        result = self.solution.levelOrder(root)

        self.assertEqual(expected_output, result)

    def test_level_order_example3(self):
        root = buildTree([])
        expected_output = []
        result = self.solution.levelOrder(root)

        self.assertEqual(expected_output, result)

if __name__ == "__main__":
    unittest.main()