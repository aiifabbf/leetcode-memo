# 二叉树的先根遍历

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = [root.val]
            if root.left:
                res += self.preorderTraversal(root.left)
            if root.right:
                res += self.preorderTraversal(root.right)
            return res
        else:
            return []