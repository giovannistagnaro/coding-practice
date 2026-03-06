import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import Optional, List
from BuildTree import buildTree
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        stack = deque([(root, (float("-inf"), float("inf")))])

        while stack:
            current_node, (curr_min, curr_max) = stack.popleft()
            if not current_node:
                continue
            current_value = current_node.val
            current_left = current_node.left
            current_right = current_node.right

            if not (curr_min < current_value < curr_max):
                return False

            if current_right:
                stack.append((current_right, [current_value, curr_max]))
            if current_left:
                stack.append((current_left, [curr_min, current_value]))

        return True
        
    #     5
    #   4   6
    # None None 3 7