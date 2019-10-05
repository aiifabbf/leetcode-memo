"""
给两个二分搜索树，问能否从第一个二分搜索树里找到一个值、从第二个二分搜索树里也找到一个值，使得这两个值加起来正好是 ``target`` 。

可以完全忽略二分搜索树的性质，直接先把第一个树遍历一遍，把里面每个值都放到一个hash set里面，然后遍历第二个树，遍历到某个 ``v`` 的时候，看 ``target - v`` 在不在hash set里面。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        return self.twoSum(self.preorderTraversal(root1), self.preorderTraversal(root2), target)
        
    def twoSum(self, array1: List[int], array2: List[int], target: int) -> bool:
        seen = set(array2) # 把第二个树里面所有的值放到set里，这样判断target - v在不在set里的复杂度是O(1)

        for v in array1: # 然后遍历第一个树里面的所有的值
            if target - v in seen: # 看target - v有没有在第二个树里面出现过，如果出现过
                return True # bingo

        return False # 找了一圈没找到

    def preorderTraversal(self, root: TreeNode) -> List[int]: # 先根方式遍历二叉树
        if root:
            res = [root.val]
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
            return res
        else:
            return []