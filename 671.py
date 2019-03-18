"""
找到二叉树里倒数第二小的节点值

这题给的二叉树有两个性质

-   要么是叶子，要么就一定有两个子节点
-   如果这个节点有两个子节点，那么这个节点的值一定小于等于两个子节点的值

当然不用这个性质也完全可以，把它当做一般二叉树，性能也没差到哪里去。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root:
            queue = [root]

            minimum = float("inf")
            secondMimimum = float("inf")

            while queue:
                levelQueue = []

                for i in queue:
                    if i.val < minimum:
                        secondMimimum = minimum
                        minimum = i.val
                    elif minimum < i.val < secondMimimum:
                        secondMimimum = i.val

                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)
                
                queue = levelQueue

            return secondMimimum if secondMimimum != float("inf") else -1
        else:
            return -1

        # 利用性质以后再说……