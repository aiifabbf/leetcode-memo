"""
二叉树的zigzag遍历

所谓zigzag遍历还是按层遍历……只是第一层从左到右、第二层从右到左这样来回往复。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            queue = [root]
            depth = 0
            res = []

            while queue:
                levelQueue = []

                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)

                if depth % 2 == 0:
                    res.append([i.val for i in queue])
                else:
                    res.append([i.val for i in queue[:: -1]])

                queue = levelQueue
                depth += 1

            return res
        else:
            return []