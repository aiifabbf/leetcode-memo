"""
把一个从小到大排好序的链表转换成一个高度平衡的二分搜索树

以前做过的是把一个从小到大排好序的array转换成一个高度平衡的二分搜索树（108题）。如果先把链表转换成array，那么这个问题就转化成了一个已经解决过的问题。
"""

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        array = self.linkedListToList(head) # 链表转换成array
        return self._sortedListToBST(array) # array转换成高度平衡二分搜索树
        
    def _sortedListToBST(self, array: List) -> TreeNode: # 把一个从小到大排好序的array变成一个高度平衡二分搜索树
        if array:
            length = len(array)
            if length == 1:
                return TreeNode(array[0])
            else:
                node = TreeNode(array[length // 2]) # 最中间元素变成根节点
                node.left = self._sortedListToBST(array[: length // 2]) # 递归地把最中间元素前面的substring变成左边子树
                node.right = self._sortedListToBST(array[length // 2 + 1: ]) # 递归地把最中间元素之后的substring变成右边子树
                return node
        else:
            return None

    def linkedListToList(self, head: ListNode) -> List: # 链表转换成array
        if head:
            res = []

            while head:
                res.append(head.val)
                head = head.next

            return res
        else:
            return []