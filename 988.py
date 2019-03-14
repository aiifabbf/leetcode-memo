# 得到所有从叶子到根的路径，并且一路把每个节点的值拼起来变成字符串，输出字典顺序最小的字符串

# 深度优先？有请257

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import string

class Solution:

    mapping = dict(zip([i for i in range(26)], string.ascii_lowercase))

    def smallestFromLeaf(self, root: TreeNode) -> str:
        paths = self.getAllPathsFromLeafToRoot(root)
        return min(paths, default="")

    def getAllPathsFromLeafToRoot(self, root: TreeNode) -> List[str]:
        if root:
            if root.left == None and root.right == None: # 叶子
                return [f"{self.mapping[root.val]}"]
            elif root.left != None and root.right == None:
                return [f"{i}{self.mapping[root.val]}" for i in self.getAllPathsFromLeafToRoot(root.left)] # 根节点出发到左边子节点、加上左边子二叉树里根节点到所有叶子的路径
            elif root.left == None and root.right != None:
                return [f"{i}{self.mapping[root.val]}" for i in self.getAllPathsFromLeafToRoot(root.right)] # 根节点出发到右边子节点、加上右边子二叉树里根节点到所有叶子的路径
            else:
                return [f"{i}{self.mapping[root.val]}" for i in self.getAllPathsFromLeafToRoot(root.left) + self.getAllPathsFromLeafToRoot(root.right)] # 左右都加
        else: # 空节点
            return [] # 无路可走