# 二叉树的中根遍历

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = []
            if root.left:
                res += self.inorderTraversal(root.left)
            res.append(root.val)
            if root.right:
                res += self.inorderTraversal(root.right)
            return res
        else:
            return []