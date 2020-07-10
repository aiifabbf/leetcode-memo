"""
把一个类似二叉树、带分支的双向链表用 **先根遍历** 展平成一个不带分支的双向链表

虽然没有特别理解是什么意思……但是看例子的感觉是DFS。可以用递归的写法，也可以把BFS里面的queue改成stack、就直接变成DFS了。
"""

from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    # def flatten(self, head: 'Node') -> 'Node':
    #     # print(self.preorderTraversal(head))
    #     array = self.preorderTraversal(head)
    #     return self.listToDoublyLinkedList(array)

    # def preorderTraversal(self, head: "Node") -> List:
    #     if head:
    #         res = [head.val] # 根节点
    #         res += self.preorderTraversal(head.child) # 左边子树
    #         res += self.preorderTraversal(head.next) # 右边子树
    #         return res
    #     else:
    #         return []

    # def listToDoublyLinkedList(self, array: List) -> "Node":
    #     if array:
    #         sentinel = Node(0, None, None, None)
    #         head = sentinel

    #         for v in array:
    #             head.next = Node(v, head, None, None) # 这里有个定时炸弹的，你想第0个节点的previous是什么？是假节点，这不就把假节点暴露了吗？
    #             head = head.next

    #         sentinel.next.prev = None # 这里一定一定不要忘了，假节点不能暴露，所以要删除第0个节点previous对假节点的应用
    #         return sentinel.next
    #     else:
    #         return None

    def flatten(self, head: 'Node') -> 'Node':
        root = head
        if root:
            sentinel = Node(None, None, None, None)
            head = sentinel
            stack = [root]

            while stack:
                node = stack.pop()
                if node.next:
                    stack.append(node.next)
                if node.child:
                    stack.append(node.child)

                head.next = Node(node.val, None, None, None)
                head.next.prev = head
                head = head.next

            if sentinel.next:
                sentinel.next.prev = None

            return sentinel.next
        else:
            return None