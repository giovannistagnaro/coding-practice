import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        k_tracker = k
        def dfs_inorder(node):
            nonlocal k_tracker
            if node.left:
                val = dfs_inorder(node.left)
                if val is not None:
                    return val
            k_tracker -= 1
            if k_tracker == 0:
                return node.val
            if node.right:
                val = dfs_inorder(node.right)
                if val is not None:
                    return val
        
        val = dfs_inorder(root)
        return val