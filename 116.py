"""
在一个 完美二叉树_ 里，给同一层的节点确定next的指向。

.. _完美二叉树: https://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees

我猜大概是方便按层遍历吧。
"""

from typing import *

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            queue = [root]
            
            while queue:
                levelQueue = []
                length = len(queue)

                for i, v in enumerate(queue):
                    if i == length - 1:
                        v.next = None
                    else:
                        v.next = queue[i + 1]
                    if v.left:
                        levelQueue.append(v.left)
                    if v.right:
                        levelQueue.append(v.right)

                queue = levelQueue

            return root
        else:
            return root