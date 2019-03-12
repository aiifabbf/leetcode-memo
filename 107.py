# 从底到根、从左到右遍历树

# 神经病啊……直接广度优先再把array倒一下不就好了？

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root:
            queue = [root]
            res = []
            while queue:
                levelQueue = []
                res.append([i.val for i in queue])
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)
                queue = levelQueue
            return res[:: -1]
        else:
            return []