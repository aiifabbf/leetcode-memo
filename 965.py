from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool: # 每一层都只验证自己和子节点是否相等
        if root: # 如果传进来的不是null
            if root.left and root.right: # 如果两个子节点都存在
                return root.left.val == root.right.val == root.val and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            elif root.left: # 只存在左子节点
                return root.left.val == root.val and self.isUnivalTree(root.left)
            elif root.right: # 只存在右子节点
                return root.right.val == root.val and self.isUnivalTree(root.right)
            else: # 子节点不存在
                return True
        else:
            return True
