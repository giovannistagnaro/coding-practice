import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        dfs_stack = [[root, 1]]
        max_size = 1

        while dfs_stack:
            [curr_node, curr_size] = dfs_stack.pop()
            if curr_node.right:
                dfs_stack.append([curr_node.right, curr_size + 1])
            if curr_node.left:
                dfs_stack.append([curr_node.left, curr_size + 1])
            if not curr_node.right and not curr_node.left:
                max_size = max(max_size, curr_size)
        
        return max_size

