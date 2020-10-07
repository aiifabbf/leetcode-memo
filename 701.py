"""
.. default-role:: math

往二分搜索树里插入数字

用函数式、递归的思路，写出来超级优雅。既然是函数式，就不要再想着命令式那种 **修改** 的方式了，应该用映射的角度来想问题。原先的BST和将要插入的数字会产生什么奇妙的化学反应呢？

定义一个函数，把原先的二分搜索树、将要插入的数字，映射到插入之后的二分搜索树

::

    f(root: Option<TreeNode>, value: i32) -> Option<TreeNode>

一个数字将要被插入到二分搜索树里，总共有两种情况

-   这个二分搜索树本身就是空的

    那么返回一棵只有一个根节点的二分搜索树，根节点的值就是插入的那个数字。

-   这个二分搜索树不是空的

    判断一下数字应该插入到左边子树还是右边子树，如果应该插入到左边子树，那么返回一棵新的树，根节点的值不变，左边子树变成新的、映射后的左边子树，右边子树不变。
"""

from typing import *

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if val < root.val: # 应该插入到左边子树
                return TreeNode(root.val, self.insertIntoBST(root.left, val), root.right) # 返回一棵新的树，根节点值、右边子树不变，左边子树是新的映射后的树
            elif val > root.val: # 右边同理
                return TreeNode(root.val, root.left, self.insertIntoBST(root.right, val))
        else:  # 空树
            return TreeNode(val) # 直接插
