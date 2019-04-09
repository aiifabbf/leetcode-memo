"""
找到二分搜索树里两个值之间的最小差值。

实在没有想到什么很好的办法，就先把二分搜索树用中根遍历变成一个从小到大排好序的array，再遍历一边这个array，找到这个array的差分的最小值。

.. 看了评论，好像也只能这么做了，我的做法的复杂度阶数和他们是一样的，但是遍历了两遍，那好像也不亏。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        array = self.inorderTraversal(root)
        return min(array[i + 1] - array[i] for i in range(len(array) - 1))

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = []
            if root.left:
                res += self.inorderTraversal(root.left)
            res += [root.val]
            if root.right:
                res += self.inorderTraversal(root.right)
            return res
        else:
            return []