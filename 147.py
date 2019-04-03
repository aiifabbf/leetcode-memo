"""
用插入排序方法给一个链表排序

小聪明，先转成list再排序再转回去……然后我发现速度最快的人都是这么玩的。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
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