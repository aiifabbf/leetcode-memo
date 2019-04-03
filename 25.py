"""
以k个节点为单位，颠倒链表中的元素

比如以3为单位颠倒 ``[1, 2, 3, 4, 5]`` ，会得到 ``[3, 2, 1, 4, 5]`` 。如果有某一组不满k个，就保持原样。

算是24题的进阶版。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        array = self.linkedListToList(head)
        
        for i in range(len(array) // k):
            array[k * i: k * (i + 1)] = array[k * i: k * (i + 1)][:: -1]

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