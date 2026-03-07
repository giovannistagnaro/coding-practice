import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree, isEqual

class TestConstructBSTFromPreAndInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_construct_BST_example1(self):
        preorder = [1,2,3,4]
        inorder = [2,1,3,4]
        expected_result = buildTree([1,2,3,None,None,None,4])

        result = self.solution.buildTree(preorder, inorder)
        self.assertTrue(isEqual(expected_result, result))

    def test_construct_BST_example1(self):
        preorder = [1]
        inorder = [1]
        expected_result = buildTree([1])

        result = self.solution.buildTree(preorder, inorder)
        self.assertTrue(isEqual(expected_result, result))

if __name__ == "__main__":
    unittest.main()