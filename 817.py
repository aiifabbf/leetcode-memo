"""
给一个array，问你这个array里有多少节点在另一个链表里能形成多少个聚类。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        array = self.linkedListToList(head)

    def linkedListToList(self, head: ListNode) -> List:
        if head:
            res = []

            while head:
                res.append(head.val)
                head = head.next

            return res
        else:
            return []