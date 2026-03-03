import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.right is None and root.left is None:
            return root
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root