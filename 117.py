"""
让每个节点的next指向同一层的右边一个节点。

感觉和116题没什么区别啊……
"""

from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            queue = [root]

            while queue:
                rowQueue = []

                for i, v in enumerate(queue):
                    if v.left:
                        rowQueue.append(v.left)
                    if v.right:
                        rowQueue.append(v.right)
                    if i == len(queue) - 1:
                        v.next = None
                    else:
                        v.next = queue[i + 1]

                queue = rowQueue

            return root
        else:
            return root