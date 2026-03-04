import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from collections import deque
from TreeNode import TreeNode
from typing import List, Optional


def buildTree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        current = queue.popleft()

        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root

def isEqual(tree1: TreeNode, tree2: TreeNode):
    return tree1 is tree2 if not tree1 or not tree2 else (
        tree1.val == tree2.val and
        isEqual(tree1.left, tree2.left) and
        isEqual(tree1.right, tree2.right)
    )


def printTree(root: TreeNode):
    if not root:
        return
    if root.left:
        printTree(root.left)
    print(root.val)
    if root.right:
        printTree(root.right)