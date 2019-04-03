"""
探测链表里是否存在回路
"""

from typing import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeArray = set()

        while head:
            if head in nodeArray:
                return True
            else:
                nodeArray.add(head)
                head = head.next
        
        return False