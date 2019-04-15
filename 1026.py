"""
求二叉树里祖先节点和子节点的差值的最大值。

我的思路是遍历二叉树里的每个节点，求出以这个节点为根节点的树中、根节点与所有子节点差值的最大值。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import functools

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root:
            res = 0
            queue = [root]

            while queue:
                node = queue.pop()
                res = max(node.val - self.minimum(node.left), node.val - self.minimum(node.right), self.maximum(node.left) - node.val, self.maximum(node.right) - node.val, res) # 求出以当前节点为根节点的树中、根节点和所有子节点差值的最大值
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            return res
        else:
            return 0

    @functools.lru_cache(None) # 加个cache会快很多，因为是递归
    def minimum(self, root: TreeNode) -> int: # 树中最小的节点值
        if root:
            res = root.val
            return min(res, self.minimum(root.left), self.minimum(root.right))
        else:
            return float("inf")

    @functools.lru_cache(None)
    def maximum(self, root: TreeNode) -> int: # 树中最大的节点值
        if root:
            res = root.val
            return max(res, self.maximum(root.left), self.maximum(root.right))
        else:
            return float("-inf")