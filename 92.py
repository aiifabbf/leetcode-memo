"""
颠倒链表的第m到第n个元素

偷个懒，讲道理速度也不差。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        array = self.linkedListToList(head)
        array[m - 1: n] = array[m - 1: n][:: -1]
        return self.listToLinkedList(array)
        
    def linkedListToList(self, head: ListNode) -> List:
        if head:
            res = []

            while head:
                res.append(head.val)
                head = head.next

            return res
        else:
            return []

    def listToLinkedList(self, array: List) -> ListNode:
        if array:
            head = ListNode(0)
            sentinel = head

            for v in array:
                head.next = ListNode(v)
                head = head.next

            return sentinel.next
        else:
            return None