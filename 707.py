"""
实现链表

不用看答案就知道最快的肯定是直接用py的list……

但是为了真正学会算法和数据结构，我这里还是认真了一下，写了个真链表。
"""

from typing import *

class MyLinkedList:

    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sentinel = MyLinkedList.ListNode(0) # 在链表开头弄个假节点，这样方便一点，sentinel.next是最开头的节点

    def get(self, index: int) -> int: # 得到第i个元素的值
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        head = self.sentinel.next # head一开始指向第0个节点
        i = 0 # 记录index

        while head:
            if i == index:
                return head.val
            else:
                head = head.next
                i += 1 # 不要忘记增加i
        
        return -1 # 找了一圈都没找到

    def addAtHead(self, val: int) -> None: # 在开头插入节点
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = MyLinkedList.ListNode(val) # 欲插入的节点
        node.next = self.sentinel.next # 先把这个欲插入的节点的next指向最开头的节点
        self.sentinel.next = node # 假节点的next指向欲插入的节点，这个欲插入的节点才正式被加入到链表当中

    def addAtTail(self, val: int) -> None: # 在链表最后追加节点
        """
        Append a node of value val to the last element of the linked list.
        """
        # head = self.sentinel # head要指向假节点，因为如果链表此时为空，假节点的next会是null。

        # while head.next:
        #     head = head.next
        
        # # 退出while的时候，head.next是null，此时head正好就是链表最后一个节点
        # head.next = MyLinkedList.ListNode(val)
        # 一改：这样写失去了一种一致性，毕竟我习惯head一开始永远指向链表最开头的节点

        head = self.sentinel.next
        previous = self.sentinel

        while head:
            previous = head
            head = head.next

        # 退出while的时候，head是null，previous正好就是链表的最后一个节点
        previous.next = MyLinkedList.ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None: # 在第i个节点之前插入一个节点
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        head = self.sentinel.next
        previous = self.sentinel
        i = 0

        while head:
            if i == index: # head此时正好就是第i个节点了，previous正好就是第i-1个节点
                node = MyLinkedList.ListNode(val)
                previous.next = node # 把previous.next指向欲插入的节点
                node.next = head # 把欲插入的节点的next指向原第i个节点
                return
            else:
                previous = head
                head = head.next
                i += 1

        # 退出while的时候，head已经是null了，previous正好是链表的最后一个节点。但是不是就直接结束了，还有一个corner case要考虑，就是如果index正好是链表的长度的时候， **插入** 与 **在链表最后追加节点** 等价。
        if i == index: # 此时head是null，previous是链表的最后一个节点
            previous.next = MyLinkedList.ListNode(val)
        else: # 说明index非法
            return

    def deleteAtIndex(self, index: int) -> None: # 删除第i个节点
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        head = self.sentinel.next
        previous = self.sentinel
        i = 0

        while head:
            if i == index: # 此时head是第i个节点，previous是第i-1个节点
                previous.next = head.next # 直接跨过第i个节点，把第i-1个节点和后面的第i+1个节点连起来。
                return
            else:
                i += 1
                previous = head
                head = head.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# s = MyLinkedList()
# s.addAtHead(1)
# print(s.get(0))
# print(s.get(1))
# print()

# s.addAtTail(3)
# print(s.get(0))
# print(s.get(1))
# print(s.get(2))
# print()

# s.addAtIndex(1, 2)
# print(s.get(0))
# print(s.get(1))
# print(s.get(2))
# print(s.get(3))
# print()

# s.deleteAtIndex(1)
# print(s.get(0))
# print(s.get(1))
# print(s.get(2))
# print()

# s.deleteAtIndex(0)
# print(s.get(0))
# print(s.get(1))
# print()

# s.deleteAtIndex(0)
# print(s.get(0))
# print(s.get(1))

# s.addAtHead(1)
# print(s.get(0))
# s.addAtIndex(1, 2)
# print(s.get(1))