"""
合并k个排好序的链表

我想到了几种方法

-   先全部转成list，合并，排好序，再转成链表

    可行

-   写一个只能给两个链表排序的函数，然后用reduce

    不可行，超时

-   写一个只能给两个链表排序的函数，然后分治

    可行，而且挺快的

-   直接合并

    没写
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from functools import reduce

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     return self.listToLinkedList(sorted(sum(map(self.linkedListToList, lists), [])))

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
    #         sentinel = ListNode(0)
    #         head = sentinel

    #         for v in array:
    #             head.next = ListNode(v)
    #             head = head.next

    #         return sentinel.next
    #     else:
    #         return None
    # 一改：这样刷小聪明不太好吧……
        # return reduce(self.merge2Lists, lists) if lists else None
        # 二改：reduce也很慢

        length = len(lists)
        if length == 0: # 空链表
            return None
        elif length == 1: # 只有一个链表
            return lists[0]
        elif length == 2: # 只有两个链表
            return self.merge2Lists(*lists) # 直接合并
        else: # 有两个以上链表
            return self.merge2Lists(self.mergeKLists(lists[: length // 2]), self.mergeKLists(lists[length // 2: ])) # 递归地、拆成两组，直到每组只有两个以下链表，然后合并、合并、再合并，直到变成一个链表

        # heads = [v[0] for v in lists]

        # while not any(None in heads):
    def merge2Lists(self, p: ListNode, q: ListNode) -> ListNode: # 合并两个排好序的链表
        sentinel = ListNode(0)
        head = sentinel

        while p != None and q != None:
            if p.val < q.val:
                head.next = ListNode(p.val)
                p = p.next
            else:
                head.next = ListNode(q.val)
                q = q.next
            head = head.next

        if p == None:
            head.next = q
        else:
            head.next = p
        return sentinel.next