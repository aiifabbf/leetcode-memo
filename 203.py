"""
删掉链表里所有值为val的节点

直接用遍历链表的方式做也不难。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0) # 建个假节点，方便一点
        sentinel.next = head
        previous = sentinel

        while head: # 这里还是遍历链表的老套路，只是变了doSomething部分
            if head.val == val: # 节点值等于val
                previous.next = head.next # 删掉当前这个节点，把前一个节点的next指向下一个节点就可以了
            else: # 不等于val
                previous = head # 当前节点变成`前一个节点`
            head = head.next # 继续遍历下一个节点

        return sentinel.next # 不要忘了是假节点
        
    # def linkedListToList(self, head: ListNode) -> List:
    #     if head:
    #         res = []

    #         while head:
    #             res.append(head.val)
    #             head = head.next

    #         return res
    #     else:
    #         return []

    # def listToLinkedList(self, array: List) -> ListNode:
    #     if array:
    #         head = ListNode(0)
    #         sentinel = head

    #         for v in array:
    #             head.next = ListNode(v)
    #             head = head.next

    #         return sentinel.next
    #     else:
    #         return None