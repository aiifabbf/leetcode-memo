"""
给一个二叉树，每个节点的值是这个节点拥有的硬币数量，每次操作只能把一个硬币移动一个单位距离，比如从根节点移到左边子节点、从左边子节点移到根节点 [#]_ 。问你最少要多少次操作，才能让每个节点恰好有一个硬币。

.. [#] 从左边子节点移到右边子节点被视为两次操作，因为首先你要把硬币从左边子节点移到根节点，再从根节点移到右边子节点。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int: