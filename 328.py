"""
重新排列链表节点，把所有下标（下标从1开始数）是奇数的节点按顺序放到最前面、所有下标是偶数的节点按顺序接到奇数链表的后面。
"""

from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            nodeArray = []

            while head:
                nodeArray.append(head)
                head = head.next

            nodeArray = nodeArray[:: 2] + nodeArray[1:: 2]

            for i, v in enumerate(nodeArray[: -1]):
                v.next = nodeArray[i + 1]
            
            nodeArray[-1].next = None
            return nodeArray[0]
        else:
            return head