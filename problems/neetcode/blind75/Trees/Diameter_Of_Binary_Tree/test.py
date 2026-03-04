import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree

class TestDiameterOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_diameter_of_binary_tree_example1(self):
        root = buildTree([1,None,2,3,4,5])
        expected_result = 3
        result = self.solution.diameterOfBinaryTree(root)

        self.assertEqual(expected_result, result)

    def test_diameter_of_binary_tree_example2(self):
        root = buildTree([1,2,3])
        expected_result = 2
        result = self.solution.diameterOfBinaryTree(root)

        self.assertEqual(expected_result, result)

    def test_diameter_of_binary_tree_empty(self):
        root = buildTree([])
        expected_result = 0
        result = self.solution.diameterOfBinaryTree(root)

        self.assertEqual(expected_result, result)

    def test_diameter_of_binary_tree_single(self):
        root = buildTree([1])
        expected_result = 0
        result = self.solution.diameterOfBinaryTree(root)

        self.assertEqual(expected_result, result)

    def test_diameter_of_binary_tree_all_one_side(self):
        root = buildTree([1,None,2,None,3,None,4,None,5])
        expected_result = 4
        result = self.solution.diameterOfBinaryTree(root)

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()