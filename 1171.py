"""
.. default-role:: math

不停地去掉链表里累加和为0的substring，直到不存在累加和为0的substring为止。

去掉累加和为0的substring很简单，用经典的积分配合hash map来做就好了，可以做到 `O(n)`

1.  给原array做一次积分，同时用一个hash map存之前见过的积分项和出现的位置
2.  遍历每个积分项 `I_j` ，看之前有没有遇到过值相同的积分项，如果遇到了某个 `i < j, I_i = I_j` ，说明 ``a[i: j]`` 这个substring的累加和是0

那么“不存在累加和为0的substring”这个条件怎么判断？看一次操作之后array的长度有没有发生变化就好了，如果array的长度没有变化，就说明array里已经不存在累加和是0的substring了。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import itertools

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        array = self.linkedListToList(head) # 先把链表变成list

        while True:
            integral = [0] + list(itertools.accumulate(array)) # 做一次积分
            seen = {
                0: 0
            } # 用hash map存一下之前见过的积分值、出现的位置
            left = -1 # 累加和是0的substring的左边界
            right = -1 # 累加和是0的substring的右边界

            for i, v in enumerate(integral[1: ], 1): # 遍历每个积分项
                if v in seen: # 对每个积分项，看一看前面有没有出现相等的积分项，如果出现了，那么说明有一段substring的累加和是0
                    left = seen[v] # 记下左边界
                    right = i # 记下右边界
                    break # 跳出循环
                else:
                    seen[v] = i

            if left >= right: # 说明没有找到累加和是0的substring
                break # 结束
            else: # 找到了一个累加和是0的substring
                array[left: right] = [] # 把这个substring从array里面去掉

        return self.listToLinkedList(array) # 再把list变回链表
        
    def linkedListToList(self, head: ListNode) -> list:
        if head:
            res = []

            while head:
                res.append(head.val)
                head = head.next
            
            return res
        else:
            return []

    def listToLinkedList(self, array: list) -> ListNode:
        if array:
            head = ListNode(0)
            sentinel = head

            for v in array:
                head.next = ListNode(v)
                head = head.next

            return sentinel.next
        else:
            return None

# s = Solution()
# print(s.linkedListToList(s.removeZeroSumSublists(s.listToLinkedList([1, 2, 3, -3, 1]))))
# print(s.linkedListToList(s.removeZeroSumSublists(s.listToLinkedList([1, 2, 3, -3, 4]))))
# print(s.linkedListToList(s.removeZeroSumSublists(s.listToLinkedList([1, 2, 3, -3, -2]))))