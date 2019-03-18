"""
计算二叉树的周长。

所谓周长是二叉树里任意两点之间路径的最长距离。

一开始的想法肯定是递归，但是这道题我想不出大问题和子问题之间有什么关联，其中有一个很明显的矛盾是，左边子树或者右边子树各自的周长，不一定是一条单向路径。换句话说，整个树的周长的计算，不一定会带上根节点。

我想出来的做法是，遍历树里面的每一个子树，计算出每个子树中一定经过根节点的最长路径的长度。对于一个树，一定经过根节点的最长路径的长度就很好算了，直接就是从根节点出发，往左尽可能向下走、往右尽可能向下走，把两个距离加起来。

这个做法是真的很慢……
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            res = 0

            while queue: # 遍历每个子树
                levelQueue = []

                for i in queue:
                    maximumDiameter = 0
                    if i.left:
                        # maximumDiameter += 1 + self.longestDownwardPathLength(i.left) # 从根节点出发、左边单向路径长度
                        maximumDiameter += self.depth(i.left)
                        levelQueue.append(i.left)
                    if i.right:
                        # maximumDiameter += 1 + self.longestDownwardPathLength(i.right) # 从根节点出发、右边单向路径长度
                        maximumDiameter += self.depth(i.right)
                        levelQueue.append(i.right)
                    res = max(maximumDiameter, res) # 和现存最长比较
                
                queue = levelQueue

            return res
        else:
            return 0

    # @functools.lru_cache() # 不加这个的话时间真的没法看了……
    # def longestDownwardPathLength(self, root: TreeNode) -> int: # 计算出一个子树从根节点出发最长的单向向下路径的长度。其实就是算出一个树的深度-1。
    #     if root:
    #         queue = [root]
    #         depth = 0

    #         while queue:
    #             depth += 1
    #             levelQueue = []

    #             for i in queue:
    #                 if i.left:
    #                     levelQueue.append(i.left)
    #                 if i.right:
    #                     levelQueue.append(i.right)

    #             queue = levelQueue

    #         return depth - 1
    #     else:
    #         return 0

    @functools.lru_cache()
    def depth(self, root: TreeNode) -> int: # 树的深度和从根节点出发往下尽可能走的距离就差1
        if root:
            return 1 + max(self.depth(root.left), self.depth(root.right))
        else:
            return 0