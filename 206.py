"""
颠倒一个链表

一开始写了两个helper function，一个把链表转成list、一个把list转成链表……后来想想不太好，就用迭代又写了个中规中矩的，结果发现速度一样。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # return self.listToLinkedList(self.linkedListToList(head)[:: -1])
        if head:
            sentinel = None # 指前一个节点

            while head:
                tempSentinel = ListNode(head.val) # 先生成当前这个节点
                tempSentinel.next = sentinel # 把当前节点的next指针指向前一个节点
                sentinel = tempSentinel # 前一个节点变成了当前的这个节点
                head = head.next # 继续遍历下一个节点

            return sentinel
        else:
            return None
        
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