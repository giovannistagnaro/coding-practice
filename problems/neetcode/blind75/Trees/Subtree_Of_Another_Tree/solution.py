import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import Optional

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot or not root:
            return False
        
        def isSameTree(node1, node2):
            return node1 is node2 if not node1 or not node2 else (
                node1.val == node2.val and
                isSameTree(node1.left, node2.left) and
                isSameTree(node1.right, node2.right)
            )
        
        target = subRoot.val
        def dfs(node):
            sameTree = False
            if not node:
                return False
            if node.val == target:
                sameTree = isSameTree(node, subRoot)
            
            return sameTree or dfs(node.left) or dfs(node.right)
        
        return dfs(root)