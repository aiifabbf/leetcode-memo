"""
两个十进制被加数的每一位放在两个链表里，要你加这两个数，把结果的每一位放在另一个链表里。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1AsList = self.linkedListToList(l1)
        number2AsList = self.linkedListToList(l2)
        number1 = int("".join(map(str, number1AsList)))
        number2 = int("".join(map(str, number2AsList)))
        return self.listToLinkedList(list(map(int, str(number1 + number2))))
        
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