# 二叉树的后根遍历

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = []
            if root.left:
                res += self.postorderTraversal(root.left)
            if root.right:
                res += self.postorderTraversal(root.right)
            res.append(root.val)

            return res
        else:
            return []