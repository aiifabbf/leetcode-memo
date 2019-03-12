# 树的先根遍历

from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            res = [root.val]
            for i in root.children:
                res += self.preorder(i)
            
            return res
        else:
            return []