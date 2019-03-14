# 获得二叉树的最大宽度。要考虑null

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # if root:
        #     queue = [root]
        #     maxWidth = 1
        #     while queue:
        #         for index, value in enumerate(queue):
        #             if value:
        #                 break
        #         firstNonNullPosition = index
        #         for index,value in list(enumerate(queue))[::-1]:
        #             if value:
        #                 break
        #         lastNonNullPosition = index
        #         maxWidth = max(maxWidth, lastNonNullPosition - firstNonNullPosition + 1)
        #         levelQueue = []
        #         for i in queue:
        #             if i:
        #                 levelQueue.append(i.left)
        #                 levelQueue.append(i.right)
        #             else:
        #                 levelQueue.append(None)
        #                 levelQueue.append(None)
                
        #         queue = levelQueue if any(i != None for i in levelQueue) else []
        #     return maxWidth
        # else:
        #     return 0
        # 一改：memory limit exceed

        