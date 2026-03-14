import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = float('-inf')

        def calc(root):
            nonlocal max_val
            if not root:
                return 0
            
            left, right = max(calc(root.left), 0), max(calc(root.right), 0)
            max_val = max(max_val, left + root.val + right)
            return root.val + max(left, right)
        
        val = calc(root)
        max_val = max(max_val, val)
        return max_val