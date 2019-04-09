"""
二叉树的最大路径和。

路径的限制只有一个，就是至少要经过一个节点，路径可以不经过根节点，可以不是单向的。
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
    def maxPathSum(self, root: TreeNode) -> int:
        queue = [root]
        maximumSum = root.val

        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            maximumSum = max(maximumSum, self.maxPathSumThroughRoot(node)) # 算出经过每个节点的

        return maximumSum

    def maxPathSumThroughRoot(self, root: TreeNode) -> int: # 经过根节点的所有路径的最大路径和
        if root:
            if root.left == None and root.right == None:
                return root.val
            elif root.left != None and root.right == None:
                return max(root.val, root.val + self.maxPathSumFromRoot(root.left))
            elif root.left == None and root.right != None:
                return max(root.val, root.val + self.maxPathSumFromRoot(root.right))
            else:
                return max(root.val, root.val + self.maxPathSumFromRoot(root.left), root.val + self.maxPathSumFromRoot(root.right), root.val + self.maxPathSumFromRoot(root.left) + self.maxPathSumFromRoot(root.right))
        else:
            return 0

    @functools.lru_cache(None)
    def maxPathSumFromRoot(self, root: TreeNode) -> int: # 从根节点出发的所有路径的最大路径和
        if root:
            return max(root.val, root.val + self.maxPathSumFromRoot(root.left), root.val + self.maxPathSumFromRoot(root.right))
        else:
            return 0