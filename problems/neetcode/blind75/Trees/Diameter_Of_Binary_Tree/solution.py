import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import Optional
from BuildTree import buildTree, isEqual

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def findDiameter(node):
            if not node:
                return 0
            r_height = l_height = 0
            if node.left:
                l_height = 1 + findDiameter(node.left)
            if node.right:
                r_height = 1 + findDiameter(node.right)

            diam = r_height + l_height
            self.max_d = max(self.max_d, diam)
            return max(r_height, l_height)
        self.max_d = 0
        findDiameter(root)
        return self.max_d
