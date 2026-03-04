import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from solution import Solution
from BuildTree import buildTree, isEqual

class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subtree_of_another_tree_example1(self):
        tree1 = buildTree([1,2,3,4,5])
        tree2 = buildTree([2,4,5])

        self.assertTrue(self.solution.isSubtree(tree1, tree2))
        
    def test_same_binary_tree_example2(self):
        tree1 = buildTree([1,2,3,4,5,None,None,6])
        tree2 = buildTree([2,4,5])

        self.assertFalse(self.solution.isSubtree(tree1, tree2))

    def test_same_binary_tree_singles(self):
        tree1 = buildTree([1])
        tree2 = buildTree([1])

        self.assertTrue(self.solution.isSubtree(tree1, tree2))

    def test_same_binary_tree_small(self):
        tree1 = buildTree([1,1])
        tree2 = buildTree([1])

        self.assertTrue(self.solution.isSubtree(tree1, tree2))

if __name__ == "__main__":
    unittest.main()