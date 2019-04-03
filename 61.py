"""
把链表的最后一个元素放到最前面，重复k次
"""

from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head:
            nodeArray = []

            while head:
                nodeArray.append(head)
                head = head.next

            length = len(nodeArray) # 得到整个链表的长度
            realRotateTimes = k % length # 循环length的倍数次等于没循环
            nodeArray[-1].next = nodeArray[0] # 变成循环链表
            nodeArray[(length - realRotateTimes - 1) % length].next = None # 沿线剪开
            return nodeArray[(length - realRotateTimes) % length] # 返回断点之后的那个节点
        else:
            return head