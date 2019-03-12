# 从左到右得到二叉树的所有叶子的值，形成一个array。判断两个二叉树的这个array是否相同。

# 我的思路是先取得两个二叉树从左到右所有叶子的array，再比较这两个array是否相等。

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = self.getLeaves(root1)
        leaves2 = self.getLeaves(root2)
        return leaves1 == leaves2
        
    def getLeaves(self, root: TreeNode) -> List[int]: # 取得一棵树所有的叶子
        if root:
            if root.left == None and root.right == None:
                return [root.val]
            res = []
            if root.left:
                res += self.getLeaves(root.left)
            if root.right:
                res += self.getLeaves(root.right)
            return res
        else:
            return []