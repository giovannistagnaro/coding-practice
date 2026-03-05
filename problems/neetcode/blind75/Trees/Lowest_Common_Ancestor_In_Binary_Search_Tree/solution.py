import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import List

class Solution_One:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def findPath(node: TreeNode, target: int, path: List[TreeNode]):
            if not node:
                return path
            
            path.append(node)

            if node.val == target:
                return path
            elif target > node.val:
                return findPath(node.right, target, path)
            else:
                return findPath(node.left, target, path)
            
        pPath = findPath(root, p.val, [])
        qPath = findPath(root, q.val, [])


        pPointer = len(pPath) - 1
        qSet = set([x for x in qPath])

        while pPointer >= 0:
            if pPath[pPointer] in qSet:
                return pPath[pPointer]
            else:
                pPointer -= 1
        return None

# cleaner solution
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
       if not root or not p or not q:
           return None
       
       if max(p.val, q.val) < root.val:
           return self.lowestCommonAncestor(root.left, p, q)
       elif min(p.val, q.val) > root.val:
           return self.lowestCommonAncestor(root.right, p, q)
       else:
           return root