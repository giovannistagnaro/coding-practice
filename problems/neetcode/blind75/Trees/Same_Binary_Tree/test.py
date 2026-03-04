import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree, isEqual

class TestSameBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_same_binary_tree_example1(self):
        tree1 = buildTree([1,2,3])
        tree2 = buildTree([1,2,3])

        self.assertTrue(self.solution.isSameTree(tree1, tree2))
        
    def test_same_binary_tree_example2(self):
        tree1 = buildTree([4,7])
        tree2 = buildTree([4,None,7])

        self.assertFalse(self.solution.isSameTree(tree1, tree2))

    def test_same_binary_tree_example3(self):
        tree1 = buildTree([1,2,3])
        tree2 = buildTree([1,3,2])

        self.assertFalse(self.solution.isSameTree(tree1, tree2))

if __name__ == "__main__":
    unittest.main()