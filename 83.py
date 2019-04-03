"""
删掉从小到大排好序的链表中重复的节点，使每个节点值只出现一次。

比82题简单多了，不用任何flag，只要记录上一个节点就可以了。

具体做法是，每次遇到一个节点，如果发现当前节点和上一个节点的值相同，就把上一个节点的next指向当前节点的下一个节点，再往下遍历；如果发现当前节点和上一个节点的值不同，把当前节点记为 **上一个节点** ，然后往下遍历就好了。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            originalHead = head # 要存下链表头省得到时候找不到了……
            previous = head
            head = head.next # 从第二个节点开始遍历

            while head:
                if head.val == previous.val: # 当前节点值和上一个节点的值相同
                    previous.next = head.next # 直接把上一个节点的next指向当前节点的下一个节点。此外，因为当前节点被删除了，所以previous不需要动
                else: # 当前节点值和上一个节点值不同
                    previous = head # 无事发生。previous记录一下，记为当前节点，给下一个节点用作判断
                head = head.next

            return originalHead
        else:
            return head