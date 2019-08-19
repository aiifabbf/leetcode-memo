"""
求二叉树每一层的和，和最大的那一层是第几层？如果有多个层的和都是最大和，返回最小的层数。

很简单，广度优先、按层遍历，求出每一层的和，然后取最大就好了。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root:
            queue = [root] # 广度优先遍历
            levelSummations = [] # 记录每一层的和

            while queue:
                levelSummation = 0 # 当前层的和
                levelQueue = [] # 按层遍历

                for node in queue:
                    levelSummation += node.val
                    if node.left:
                        levelQueue.append(node.left)
                    if node.right:
                        levelQueue.append(node.right)

                queue = levelQueue
                levelSummations.append(levelSummation)

            return max(enumerate(levelSummations), key=lambda v: (v[1], -v[0]))[0] + 1 # 返回和最大的那个层，如果有多个层的和都是最大和，返回小的那个。这里用了enumerate和一个custom key，先按每层和排序，再按层数的倒数排序。注意下标是从0开始的，所以最后要+1
        else:
            return 0