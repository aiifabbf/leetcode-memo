# 找到一个二叉树的最小深度，也就是所有叶子的最浅深度

# 应该还是广度优先吧，找到第一个left和right都为null的node

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root: # 确定存在根节点
            depth = 1 # 已知深度
            queue = [root] # 因为确定存在根节点所以已知深度是1
            while queue:
                levelQueue = []
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right: # 这里一定不是elif……切记
                        levelQueue.append(i.right)
                    if i.left == None and i.right == None:
                        return depth
                queue = levelQueue
                depth += 1
            return depth - 1
        else:
            return 0