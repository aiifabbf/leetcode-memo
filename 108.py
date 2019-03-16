"""
把已经排好序的array变成一个二分搜索树BST，而且要求是height-balanced BST。

height-balanced BST好像就是平衡二叉树的意思。110题也提到了平衡二叉树的判定。

.. note::
    
    一个BST，如果用中根遍历，会得到一个从小到大排好序的array。

数组到普通的BST是很简单的，最简单的就是右单链一直下去……但是这样的BST好像没有什么意义，查找复杂度还是\ :math:`O(n)`\ ，所以要求要高度平衡，这样复杂度可以降到\ :math:`O(\log n)`\ 。

一个直观的想法是\ [#]_\ 把数组最中间一个数作为根节点，这个最中间节点左边的数组变成一个平衡BST，作为根节点的左边子树，右边的数组也变成一个平衡BST，作为根节点的右边子树。

.. [#]　我也不知道为什么直观，但是我突然就想到了，而且我也没法证明给你看为什么这样做就真的可以做到平衡……

"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: # 空树
            return None
        elif len(nums) == 1: # 数组只含一个元素
            return TreeNode(nums[0])
        else: # 数组含有2个及以上的元素，这时候可以继续拆
            n = len(nums)
            root = TreeNode(nums[n // 2]) # 取最中间一个元素作为根节点
            root.left = self.sortedArrayToBST(nums[0: n // 2]) # 构造左边子树
            root.right = self.sortedArrayToBST(nums[n // 2 + 1:]) # 构造右边子树
            return root