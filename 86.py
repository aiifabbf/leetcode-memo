"""
把链表里小于x的节点全部放到基准节点前面，把大于等于x的节点全部放到基准节点后面，注意保持原顺序。

这个操作在快速排序里经常用到。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        sentinel1 = ListNode(0) # 第一个分区
        head1 = sentinel1
        sentinel2 = ListNode(0) # 第二个分区
        head2 = sentinel2

        while head:
            if head.val < x: # 比x小
                head1.next = ListNode(head.val) # 追加到第一个分区
                head1 = head1.next
            else: # 大于等于x
                head2.next = ListNode(head.val) # 追加到第二个分区
                head2 = head2.next
            head = head.next

        head1.next = sentinel2.next # 把第一分区和第二分区接起来
        return sentinel1.next # 返回第一分区