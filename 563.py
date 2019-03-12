# 计算二叉树的什么tilt

# 一个节点的tilt的定义是，左子树所有节点的值之和与右子树所有节点的值之和的绝对值。一个二叉树的tilt是这个二叉树里所有节点的tilt之和

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            res = 0
            while queue:
                levelQueue = []
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)
                    res += abs(self.treeSum(i.left) - self.treeSum(i.right))
                queue = levelQueue
            return res
        else:
            return 0

    @functools.lru_cache()
    def treeSum(self, root: TreeNode) -> int:
        if root:
            return root.val + self.treeSum(root.left) + self.treeSum(root.right)
        else:
            return 0