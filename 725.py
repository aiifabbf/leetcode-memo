"""
把链表分成尽可能均匀的k组
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        nodeArray = []

        while root:
            nodeArray.append(root)
            root = root.next

        groups = nodeArray[:: max(len(nodeArray) // k, 1)]

        for i in range(k - len(groups)):
            groups.append(None)

        return groups