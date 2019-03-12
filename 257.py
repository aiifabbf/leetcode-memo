# 输出二叉树里从根节点到所有叶子的路径

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            if root.left == None and root.right == None:
                return [f"{root.val}"]
            elif root.left != None and root.right == None:
                return [f"{root.val}->{i}" for i in self.binaryTreePaths(root.left)]
            elif root.left == None and root.right != None:
                return [f"{root.val}->{i}" for i in self.binaryTreePaths(root.right)]
            else:
                return [f"{root.val}->{i}" for i in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)]
        else:
            return []