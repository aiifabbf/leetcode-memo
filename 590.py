# 后根遍历

from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root:
            res = []
            for i in root.children:
                res += self.postorder(i)
            res.append(root.val)
            
            return res
        else:
            return []