# 判断一个二叉树是不是沿y轴对称

# 一开始的想法是把左边子树先invert一下（226题，著名的homebrew作者翻车题），再和右子树比较是不是完全一致（100题）。好像时间复杂度阶数是一样的啊……

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        