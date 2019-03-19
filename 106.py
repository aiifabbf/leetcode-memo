"""
从中根遍历路径、后根遍历路径，恢复二叉树的结构。105题的补充。

先画出两种路径的分布图，方便理解，先是中根遍历路径

::

    [       ] o (       )
    ----------------------
    0       ? ? ?        n

然后是后根遍历路径

::

    [       ] (       ) o
    ----------------------
    0       ? ? ?        n

一开始无论是中根遍历还是后根遍历路径，我们都完全不清楚怎样划分左边子树、右边子树和根节点，但是观察到后根遍历路径的最后一个元素是根节点的值，再到中根遍历路径里去找根节点，确定它的位置，就可以知道左边子树、右边子树的节点个数，从而完全确定两个路径的分区划分。

再递归地恢复左边子树、右边子树的结构，就完成了。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(postorder[-1]) # 后根遍历的最后一个元素一定是根节点
            rootPosition = inorder.index(root.val) # 在中根遍历路径中找到根节点的位置，就可以确定左边子树、右边子树的大小了。
            leftTreeInorder = inorder[: rootPosition] # 先根遍历路径中，左边子树的范围是从开头到根节点前
            rightTreeInorder = inorder[rootPosition + 1: ] # 先根遍历路径中，右边子树的范围是从根节点之后到最后
            leftTreePreorder = postorder[: rootPosition] # 后根遍历路径中，左边子树的节点个数和先根遍历路径中完全相同，所以左边子树的范围也是从一开始，数一个根节点位置
            rightTreePreorder = postorder[rootPosition: -1] # 右边子树的范围是到最后一个元素之前（因为最后一个元素是根节点的值）

            root.left = self.buildTree(leftTreeInorder, leftTreePreorder)
            root.right = self.buildTree(rightTreeInorder, rightTreePreorder)
            return root
        else:
            return None