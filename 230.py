"""
从一个二分搜索树里找到第k小的元素

回想一件事情：中根遍历二分搜索树可以得到从小到大排好序的array。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root:
            inorderPath = self.inorderTraversal(root)
            # return sorted(set(inorderPath))[k - 1] # 可能会有重复？
            return inorderPath[k - 1] # 没重复的话就直接return好了
        else:
            return []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = []
            res += self.inorderTraversal(root.left)
            res += [root.val]
            res += self.inorderTraversal(root.right)
            return res
        else:
            return []