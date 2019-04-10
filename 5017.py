"""
二叉树里每个节点的值是1或0，每条从根节点到叶子节点的路径都能组成一个二进制数，求这些二进制数的和。

又是求从根节点到所有叶子节点的路径的问题，换汤不换药。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import functools

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        allPaths = self.allPathsFromRootToLeaf(root)
        return sum(map(lambda x: int(x, 2), allPaths)) % (10 ** 9 + 7) # 每条路径先转换成int，再加起来，再取模
    
    @functools.lru_cache()
    def allPathsFromRootToLeaf(self, root: TreeNode) -> List[str]: # 从根节点到叶子节点的所有路径
        if root:
            if root.left == None and root.right == None:
                return [str(root.val)]
            elif root.left == None and root.right != None:
                return [
                    str(root.val) + route for route in self.allPathsFromRootToLeaf(root.right)
                ]
            elif root.left != None and root.right == None:
                return [
                    str(root.val) + route for route in self.allPathsFromRootToLeaf(root.left)
                ]
            else:
                return [
                    str(root.val) + route for route in self.allPathsFromRootToLeaf(root.left) + self.allPathsFromRootToLeaf(root.right)
                ]
        else:
            return []