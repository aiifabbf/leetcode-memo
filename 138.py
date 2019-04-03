"""
深复制（deep copy）一个链表。

我的理解，深复制是生成一个值、结构和原来的对象一模一样的、但是又和原对象没有任何引用关系的对象。就这道题而言，不仅要生成新的节点，新的节点的值和对应原节点的值要一样以外，新节点的next和random不能指向原链表的任何一个节点，而是要指向新链表里的节点。
"""

from typing import *

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head:
            nodePositionMapping = {} # 记录原链表中节点和它们所在位置的mapping
            i = 0

            while head:
                nodePositionMapping[head] = i
                head = head.next
                i = i + 1

            # res = [Node(0, None, None)] * len(nodePositionMapping) # 这个是个大坑……py里 [x] * 10 如果x不是primitive type，那么生成的是10个x的指针
            res = [Node(0, None, None) for i in range(len(nodePositionMapping))] # 建立新链表

            for v, i in nodePositionMapping.items():
                res[i].val = v.val # 复制原节点值
                res[i].next = res[nodePositionMapping[v.next]] if v.next else None # 复制原节点next指针
                res[i].random = res[nodePositionMapping[v.random]] if v.random else None # 复制原节点random指针

            return res[0]
        else:
            return None