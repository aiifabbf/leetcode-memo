"""
两两交换链表里相邻的两个节点

比如 ``[1, 2, 3, 4]`` 变成 ``[2, 1, 3, 4]`` 。

算了……先转换成list，什么都好说。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        array = self.linkedListToList(head)
        array = sum([array[2 * i: 2 * i + 2][:: - 1] for i in range(len(array) // 2 + 1)], [])
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
            sentinel = ListNode(0)
            head = sentinel

            for v in array:
                head.next = ListNode(v)
                head = head.next

            return sentinel.next
        else:
            return None