"""
寻找二分搜索树里任意两个节点的差值的最小值

这题怎么和刚做过的783题一模一样啊……
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        array = self.inorderTraversal(root)
        return min(array[i + 1] - array[i] for i in range(len(array) - 1))
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            res = []
            if root.left:
                res += self.inorderTraversal(root.left)
            res.append(root.val)
            if root.right:
                res += self.inorderTraversal(root.right)
            return res
        else:
            return []