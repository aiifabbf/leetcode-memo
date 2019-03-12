# 找到根节点到所有叶子的路径，再把这个路径上经过的所有节点的值个十百千位放在一起转换成一个数字，把所有的数字加起来。

# 好绕啊。但是总之就是要找到根节点到所有叶子的路径，和257题差不多。

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        paths = self.binaryTreePaths(root)
        return sum(int(i) for i in paths)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            if root.left == None and root.right == None:
                return [f"{root.val}"]
            elif root.left != None and root.right == None:
                return [f"{root.val}{i}" for i in self.binaryTreePaths(root.left)]
            elif root.left == None and root.right != None:
                return [f"{root.val}{i}" for i in self.binaryTreePaths(root.right)]
            else:
                return [f"{root.val}{i}" for i in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)]
        else:
            return []