import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_index = {}
        for i, val in enumerate(inorder):
            val_to_index[val] = i
        
        pre_index = 0
        def dfs(l, r):
            nonlocal pre_index

            if l > r:
                return None
            
            pre_value = preorder[pre_index]
            pre_index += 1
            root = TreeNode(pre_value)
            mid = val_to_index[pre_value]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root


        return dfs(0, len(inorder) - 1)