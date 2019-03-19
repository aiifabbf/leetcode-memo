"""
给一个区间 :math:`[L, R]` ，删掉二分搜索树里面所有不在这个区间里的节点，同时保证删完这个二叉树还是二分搜索树。

.. 想到了刚做的450题。

.. 但是总是感觉这些题有点脏……因为有副作用。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root:
            if root.val < L: # 当前节点小于左边界，因为当前节点的左边子树里的每个节点都小于当前节点，所以左边子树里的每个节点都小于左边界，要去掉，只保留右边子树
                return self.trimBST(root.right, L, R)
            elif root.val > R: # 同理，如果当前节点大于右边界，因为当前节点的右边子树里的每个节点都大于当前节点，所以右边子树里的每个节点都大于右边界，要去掉，只保留左边子树
                return self.trimBST(root.left, L, R)
            else: # 如果当前节点值正好落在范围内，那么在这一层无法判断，要传入下一层再判断
                root.left = self.trimBST(root.left, L, R)
                root.right = self.trimBST(root.right, L, R)
                return root
        else:
            return None