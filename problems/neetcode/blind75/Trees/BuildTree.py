import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from TreeNode import TreeNode
from typing import List

def buildTree(nodes: List[int | None]) -> TreeNode:
    if not nodes or nodes[0] is None:
        return None
    
    tree_nodes = [
        TreeNode(val) if val is not None else None
        for val in nodes
    ]
    n = len(tree_nodes)

    for i in range(n):
        if tree_nodes[i] is None:
            continue

        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < n:
            tree_nodes[i].left = tree_nodes[left_i]
        if right_i < n:
            tree_nodes[i].right = tree_nodes[right_i]

    return tree_nodes[0]

def isEqual(tree1: TreeNode, tree2: TreeNode):
    return tree1 is tree2 if not tree1 or not tree2 else (
        tree1.val == tree2.val and
        isEqual(tree1.left, tree2.left) and
        isEqual(tree1.right, tree2.right)
    )