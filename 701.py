"""
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if val < root.val:
                if root.left:
                    self.insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val)
            elif val > root.val:
                if root.right:
                    self.insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)
            return root
        else: # 空树
            root = TreeNode(val) # 直接插
            return root

        # 最快的做法就是我这个做法