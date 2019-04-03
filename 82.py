"""
删掉链表里所有 **值出现重复** 的节点

要保持剩下的元素顺序不变。

我的做法是，遍历链表，一旦发现下一个节点和自己一样，先不要着急把前一个节点的next指向下一个节点，因为很有可能下一个节点和下下一个节点还是值一样。这时候，先设置一个flag，告诉下一轮上一轮遇到了重复，然后直接往下一个节点去就好了。

如果到了下一个节点，发现这个节点的下一个节点还是和自己一样，还是不要做任何事，直接往下一个结点去就好了。如果发现这个节点的下一个节点和自己不一样了，说明之前所有的节点、从最后一次遇到的不重复的节点开始、到当前这个节点之间（包括这个节点）的全部节点都要删掉，直接把指针指过来就好了，记得把flag清零。
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
            sentinel = ListNode(None) # 假节点
            sentinel.next = head
            lastUniqueNode = sentinel # lastUniqueNode存最后一次遇到的不重复的节点
            duplicateMode = False

            while head:
                if head.next: # 当前节点不是链表的最后一个节点
                    if head.next.val == head.val: # 发现下一个节点和自己一样
                        if duplicateMode: # 当前已经是duplicate mode了
                            pass # 不用做任何事，直接往下一个就可以了，直到遇见不一样的
                        else: # 当前不是duplicate mode
                            duplicateMode = True # 进入duplicate mode
                    else: # 发现下一个节点和自己不一样
                        if duplicateMode: # 如果在duplicate mode
                            lastUniqueNode.next = head.next # 上一个节点直接连到下一个
                            duplicateMode = False # 应该退出duplicate mode
                        else: # 不在duplicate mode
                            lastUniqueNode = head # 一切正常
                else: # 当前节点是链表的最后一个节点了
                    if duplicateMode:
                        lastUniqueNode.next = head.next
                        duplicateMode = False
                    else:
                        pass
                head = head.next

            return sentinel.next
        else:
            return head