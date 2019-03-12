# 检查一个树是不是二分搜索树

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            if root.left and root.right:
                return self.isValidBST(root.left) and root.left.val < root.val and self.isValidBST(root.right) and root.right.val > root.val
            elif root.left:
                return self.isValidBST(root.left) and root.left.val < root.val
            elif root.right:
                return self.isValidBST(root.right) and root.right.val > root.val
            else:
                return True
        else:
            return True