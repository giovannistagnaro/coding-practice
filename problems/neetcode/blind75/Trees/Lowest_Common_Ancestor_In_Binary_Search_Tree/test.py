import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from TreeNode import TreeNode
from solution import Solution
from BuildTree import buildTree, isEqual

class TestLowestCommonAncestorInBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lowest_common_ancestor_example1(self):
        root = buildTree([5,3,8,1,4,7,9,None,2])
        p = TreeNode(3)
        q = TreeNode(8)
        expected_result = 5

        result = self.solution.lowestCommonAncestor(root, p, q)
        if not result or not result.val:
            self.fail()
            return
        self.assertEqual(expected_result, result.val)

    def test_lowest_common_ancestor_example2(self):
        root = buildTree([5,3,8,1,4,7,9,None,2])
        p = TreeNode(3)
        q = TreeNode(4)
        expected_result = 3

        result = self.solution.lowestCommonAncestor(root, p, q)
        if not result or not result.val:
            self.fail()
            return
        self.assertEqual(expected_result, result.val)

    def test_lowest_common_ancestor_unbalanced(self):
        root = buildTree([5,None,8,None,9])
        p = TreeNode(8)
        q = TreeNode(9)
        expected_result = 8

        result = self.solution.lowestCommonAncestor(root, p, q)
        if not result or not result.val:
            self.fail()
            return
        self.assertEqual(expected_result, result.val)

    def test_lowest_common_ancestor_same(self):
        root = buildTree([5,3,8,1,4,7,9,None,2])
        p = TreeNode(9)
        q = TreeNode(9)
        expected_result = 9

        result = self.solution.lowestCommonAncestor(root, p, q)
        if not result or not result.val:
            self.fail()
            return
        self.assertEqual(expected_result, result.val)

if __name__ == "__main__":
    unittest.main()