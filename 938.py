"""
把二分搜索树里落在 [L, R] 区间内的所有节点的值都加起来

暴力全遍历肯定是可以的，但是这题的目的肯定是要你利用一下二分搜索树的特性，不然直接说二叉树不就可以了吗……
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # if root:
        #     summation = 0
        #     if root.left:
        #         summation += self.rangeSumBST(root.left, L, R)
        #     if root.right:
        #         summation += self.rangeSumBST(root.right, L, R)
        #     if L <= root.val <= R:
        #         summation += root.val
        #     return summation
        # else:
        #     return 0
        # 一改：利用一下二分搜索树的特性，稍微节省一点时间
        if root:
            summation = 0
            if root.left:
                if root.val < L: # 如果当前节点小于L，而又因为左边子树里的每个节点都比当前节点小，那么可以确定左边子树里每个节点都不在范围内，所以左边子树直接不用遍历了
                    pass
                else: # root.val >= L
                    summation += self.rangeSumBST(root.left, L, R)
            if root.right:
                if root.val > R: # 如果当前节点大于R，而又因为右边子树里每个节点都比当前节点大，那么可以确定右边子树里每个节点都不在范围内，所以右边子树整个都直接不用遍历了
                    pass
                else:
                    summation += self.rangeSumBST(root.right, L, R)
            if L <= root.val <= R:
                summation += root.val
            return summation
        else:
            return 0