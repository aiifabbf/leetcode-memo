"""
找到两个链表公共部分的第一个节点。

需要考虑各种corner case。比如

-   两个链表实际上根本没有公共部分
-   其中一个链表就是另一个链表的substring

用set就完事儿了。先走一遍链表A，把每个节点都放进set，再走一遍链表B，一边走，一边看节点在不在set里，如果在，那就是这个节点了；如果走了一遍都没有发现链表B里有哪个节点在set里，说明两个链表其实根本没有公共部分。
"""

from typing import *

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeSet = set()
        head = headA # 先走一遍链表A

        while head:
            nodeSet.add(head) # 一边走一边把每个节点都放进set
            head = head.next

        head = headB # 再走一遍链表B

        while head:
            if head in nodeSet: # 这个节点已经在set里了，说明走A的时候已经经过了
                return head # 那就是这个节点了
            else:
                # nodeSet.add(head) # 其实根本也不用把链表B里的节点加入set了
                head = head.next

        return None # 走了一遍B都没有发现B里有哪个节点在set里，说明两个链表根本没有公共部分。
