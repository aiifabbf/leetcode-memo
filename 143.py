"""
按某种顺序重排链表
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            nodeArray = []

            while head:
                nodeArray.append(head)
                head = head.next

            res = []
            i = 0

            while nodeArray: # 交替放第一个、最后一个、第一个、最后一个……
                if i % 2 == 0:
                    res.append(nodeArray.pop(0)) # 放第一个
                else:
                    res.append(nodeArray.pop()) # 放最后一个
                i += 1

            for i, v in enumerate(res[: -1]):
                v.next = res[i + 1] # 维持链表next关系

            res[-1].next = None # 不要忘了最后一个节点的next
        else:
            return None