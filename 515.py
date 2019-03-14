# 得到二叉树每一行节点的最大值

# 广度优先、按层遍历……

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root:
            queue = [root]
            res = []
            while queue:
                levelQueue = []
                levelMax = - float("inf")
                for i in queue:
                    levelMax = max(levelMax, i.val)
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)
                queue = levelQueue
                res.append(levelMax)
            return res
        else:
            return []