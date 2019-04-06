"""
返回链表最中间的那个节点。如果有两个，返回最中间两个节点的第二个。
"""

from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head:
            nodeArray = []

            while head:
                nodeArray.append(head)
                head = head.next

            # if len(nodeArray) % 2 == 0:
            #     return nodeArray[len(nodeArray) // 2]
            # else:
            #     return nodeArray[len(nodeArray) // 2]
            return nodeArray[len(nodeArray) // 2]
        else:
            return None