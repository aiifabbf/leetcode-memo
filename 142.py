"""
探测链表中的环路，返回回路开始的那个节点

如果没有环路，就返回null。

141题是只要判断链表里存不存在回路，感觉做法完全一样。
"""

from typing import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeSet = set()

        while head:
            if head in nodeSet:
                return head
            else:
                nodeSet.add(head)
                head = head.next

        return None