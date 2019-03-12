# 二叉树的广度优先、按层遍历

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            res = []
            queue = [root]
            while queue:
                levelQueue = []
                res.append([i.val for i in queue])
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)
                queue = levelQueue
            return res
        else:
            return []