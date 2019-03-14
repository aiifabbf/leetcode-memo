# 把二叉树变成右单链

# 看例子好像是先根遍历。那就先把树用先根遍历变成array，再从array重建树

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            preorderPath = self.preorderTraversal(root)
            lastNode = root
            for node in preorderPath[1: ]:
                lastNode.left = None
                lastNode.right = node
                lastNode = node
            lastNode.left = None
            lastNode.right = None
        else:
            return

    def preorderTraversal(self, root: TreeNode) -> List[TreeNode]:
        if root:
            res = [root]
            if root.left:
                res += self.preorderTraversal(root.left)
            if root.right:
                res += self.preorderTraversal(root.right)
            return res
        else:
            return []