"""
平均地随机选取链表里的某个节点

我的想法是先遍历一遍链表，转换成连续数组，再用随机数生成器产生一个随机index，拿着这个index从连续数组里取一个元素就好了。

这题还有个追问：如果链表的长度非常大怎么办。还能怎么办，先遍历一遍，但是不转换成连续数组（因为太大了啊），得到长度，用随机数生成器产生随机index，每次要生成的时候就遍历到第index到那个节点。这样虽然慢一点，但是不占用额外空间。

这里的代码写的是追问的解法。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        n = 0
        head = self.head

        while head: # 遍历链表
            head = head.next
            n += 1
        
        self.length = n # 得到链表的长度

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        index = random.randint(0, self.length - 1) # 随机生成一个[0, n - 1]里的整数index
        head = self.head

        for i in range(index): # 遍历到第index个节点
            head = head.next

        return head.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()