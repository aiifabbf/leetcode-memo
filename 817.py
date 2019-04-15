"""
给一个array，问你这个array里有多少节点在另一个链表里能形成多少个聚类。

比如给你的array是 ``[0, 1, 2, 3]`` ，再问你 ``0, 1, 3`` 这三个节点在原array里形成了多少个聚类，因为 ``0, 1`` 在原array里是相邻的，所以它们两个形成一个聚类，但是 ``3`` 和 ``0, 1`` 都不相邻，所以单独形成一个聚类。所以一共形成两个聚类。

因为G里存的是值，而不是下标，所以就先遍历链表，把每个值的下标记录在一个 ``dict`` 里，然后把G里的值全部转化成值在链表里的下标，并且排序，这样很方便就能看出哪些下标不连续。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        # array = self.linkedListToList(head)
        # valuePositionMapping = dict(zip(array, range(len(array))))
        # 可以不用转换成list
        valuePositionMapping = {} # 用一个dict存(value, position)，方便后面快速得到G中元素的下标
        i = 0

        while head:
            valuePositionMapping[head.val] = i
            head = head.next
            i += 1

        positions = sorted(map(lambda x: valuePositionMapping[x], G)) # 得到G中所有元素在原array中的位置，然后从小到大排序
        if positions == []:
            return 0
        else:
            componentCount = 1

            for i, v in enumerate(positions[1: ], 1):
                if v - positions[i - 1] != 1: # 出现了缝隙
                    componentCount += 1 # 说明当前的位置是属于下一个聚类了
                else:
                    pass

            return componentCount

    # def linkedListToList(self, head: ListNode) -> List:
    #     if head:
    #         res = []

    #         while head:
    #             res.append(head.val)
    #             head = head.next

    #         return res
    #     else:
    #         return []