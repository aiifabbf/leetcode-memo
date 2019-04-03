"""
给一个链表排序

和147差不多。
"""

from typing import *

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.listToLinkedList(sorted(self.linkedListToList(head)))
        
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
            sentinel = ListNode(0)
            head = sentinel

            for v in array:
                head.next = ListNode(v)
                head = head.next

            return sentinel.next
        else:
            return None