"""
判断一个链表是不是回文的。
"""

from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        array = self.linkedListToList(head)
        return array == array[:: -1]

    def linkedListToList(self, head: ListNode) -> List:
        if head:
            res = []

            while head:
                res.append(head.val)
                head = head.next
            
            return res
        else:
            return []