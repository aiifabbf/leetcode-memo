# 合并两个二叉树。如果两个树里同一位置的节点有一个是null，就用另一个节点替换；如果都存在，就相加

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 用递归的方法
        if t1 and t2: # t1和t2都存在
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
        elif t1: # t2不存在
            node = TreeNode(t1.val)
            node.left = self.mergeTrees(t1.left, None)
            node.right = self.mergeTrees(t1.right, None)
        elif t2: # t1不存在
            node = TreeNode(t2.val)
            node.left = self.mergeTrees(None, t2.left)
            node.right = self.mergeTrees(None, t2.right)
        else: # 两个都不存在
            node = None
        
        return node