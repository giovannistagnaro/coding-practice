import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        
        return dfs(p, q)