# 判断一个二叉树是不是另一个二叉树的子树

# 感觉有两种思路

# -   把两个树都用先根遍历一遍得到两个array，再判断一个array是不是另一个array的substring
# -   把树a的每个子树都和树b放在一起判断是否相等，如果树a存在一个子树和树b完全相等，那么说明树b是树a的子树

# 这里用了第2种思路。

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t:
            queue = [s]
            while queue:
                levelQueue = []
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)
                    if self.isEqualTree(i, t): # 判断当前子树和t是否完全相等
                        return True # 相等的话直接后面不用看了
                queue = levelQueue
            return False # 找了一圈都没有找到s的某个子树和t完全相等
        else:
            return True

    @functools.lru_cache() # 加cache快一点
    def isEqualTree(self, s: TreeNode, t: TreeNode) -> bool:
        if s != None and t != None: # 两个节点都不为空
            return s.val == t.val and self.isEqualTree(s.left, t.left) and self.isEqualTree(s.right, t.right) # 判断根节点是否相等，再判断各自左边子树是否相等、右边子树是否相等
        elif s == None and t == None: # 两个节点都为空
            return True
        else: # 一个节点空另一个不空
            return False # 肯定不相等