"""
不给你整个单链表，只给你当前节点，删掉当前节点
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # previous = node
        # while True:
        #     if node.next:
        #         node.val = node.next.val
        #     else:
        #         previous.next = None
        #         break
        #     previous = node
        #     node = node.next
        # 好像不用这么麻烦……既然不能改node前一个节点的next，那就改node的next，把node的next指到node.next.next，再把node.val改成node.next.val

        node.val = node.next.val
        node.next = node.next.next