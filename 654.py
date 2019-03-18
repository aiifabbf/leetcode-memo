"""
从array构造出满足以下性质的一种二叉树 [#]_

-   根节点的值是array中的最大元素
-   左边子树是array最大元素左边的所有元素构成的同种二叉树。即取第一个元素到最大元素之前的substring，然后按相同的规则构成二叉树
-   右边子树是array最大元素右边的所有元素构成的同种二叉树

.. [#] 这种二叉树叫做 `Cartesian Tree`_

从定义里就能看出递归的感觉……

.. _Cartesian Tree: https://en.wikipedia.org/wiki/Cartesian_tree
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums:
            if len(nums) == 1: # array只有一个元素
                return TreeNode(nums[0])
            else:
                maximumPosition = max(enumerate(nums), key=lambda x: x[1])[0] # 最大值的位置
                root = TreeNode(nums[maximumPosition]) # 根节点是array最大值
                root.left = self.constructMaximumBinaryTree(nums[: maximumPosition]) # 取左边构成树
                root.right = self.constructMaximumBinaryTree(nums[maximumPosition + 1: ]) # 取右边成树
                return root
        else:
            return None