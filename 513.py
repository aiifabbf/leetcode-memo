# 得到二叉树最后一行的最左边元素

# 广度优先、按层遍历……

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            while queue:
                levelQueue = []
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)
                if levelQueue:
                    queue = levelQueue
                else:
                    return queue[0].val
        else:
            return None