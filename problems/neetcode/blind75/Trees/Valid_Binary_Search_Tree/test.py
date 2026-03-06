import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree, isEqual

class TestValidBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_bst_example1(self):
        root = buildTree([2,1,3])
        result = self.solution.isValidBST(root)

        self.assertTrue(result)

    def test_valid_bst_example2(self):
        root = buildTree([1,2,3])
        result = self.solution.isValidBST(root)

        self.assertFalse(result)

    def test_valid_bst_single(self):
        root = buildTree([1])
        result = self.solution.isValidBST(root)

        self.assertTrue(result)

    def test_valid_bst_negatives(self):
        root = buildTree([0,-5,1,-7,-3,None,18])
        result = self.solution.isValidBST(root)

        self.assertTrue(result)

    def test_valid_bst_example4(self):
        root = buildTree([5,4,6,None,None,3,7])
        result = self.solution.isValidBST(root)

        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()