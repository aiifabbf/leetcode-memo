"""
找到链表里每个元素右边比自己大的最近的元素的值。

这题和739一模一样。用一个stack就好了。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        T = self.linkedListToList(head)
        stack = []
        res = [0] * len(T)

        for i, v in enumerate(T):
            if stack:

                while True:
                    if stack:
                        day = stack.pop()
                        if v > day[1]:
                            res[day[0]] = v # 这里和739不一样，改成符合题目要求的就好了
                        else:
                            stack.append(day)
                            stack.append((i, v))
                            break
                    else:
                        stack.append((i, v))
                        break

            else:
                stack.append((i, v))
        return res

    def linkedListToList(self, head: ListNode) -> List[int]: # 链表真是麻烦，先转成list……
        if head:
            res = []

            while head:
                res.append(head.val)
                head = head.next

            return res
        else:
            return []

# s = Solution()
# print()