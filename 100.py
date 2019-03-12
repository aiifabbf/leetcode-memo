# 检查两个二叉树是否完全相同

# 提示用深度优先……但是好像广度优先也不错啊，难道有什么深层次的统计学意义在里面吗……

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p == None and q == None:
            return True
        else:
            return False