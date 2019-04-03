"""
从链表中删除倒数第n个节点
"""

from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head:
            nodeArray = []

            while head:
                nodeArray.append(head)
                head = head.next

            nodeArray.pop(-n) # 删掉倒数第n个节点

            if nodeArray: # 删掉之后有可能整个链表就没了，所以要处理

                for i, v in enumerate(nodeArray[: -1]): # 维持链表next关系
                    v.next = nodeArray[i + 1]
                
                nodeArray[-1].next = None
                return nodeArray[0]
            else:
                return None
        else:
            return None