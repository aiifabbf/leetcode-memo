"""
二叉树的后根遍历
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if root:
    #         res = []
    #         if root.left:
    #             res += self.postorderTraversal(root.left)
    #         if root.right:
    #             res += self.postorderTraversal(root.right)
    #         res.append(root.val)

    #         return res
    #     else:
    #         return []

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            stack = [root]
            res = []

            while stack:
                node = stack.pop()
                if node.left: # 先放左边
                    stack.append(node.left)
                if node.right: # 再放右边
                    stack.append(node.right)

                res.append(node)

            return res[:: -1] # 最后颠倒
        else:
            return []