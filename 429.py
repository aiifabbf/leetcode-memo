# 树的广度优先遍历

from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root:
            result = []
            queue = [root]
            while queue:
                levelResult = [i.val for i in queue]
                levelQueue = sum((i.children for i in queue), [])

                result.append(levelResult)
                queue = levelQueue

            return result
        else:
            return []