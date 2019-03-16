"""
从先根遍历、中根遍历路径推测出树的结构。

首先先根遍历路径的第一个元素就是根节点的值。据此再到中根遍历路径的里找到根节点所在的位置，这样就完全确定了中根遍历路径里左边子树、根节点、右边子树的范围，有了这个范围之后，先根遍历路径里的对应的范围也能全部确定。

然后再通过同样的方法，递归地把左边子树、右边子树恢复出来。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root = TreeNode(preorder[0]) # 先根遍历路径的第一个元素肯定是根节点
            rootPosition = inorder.index(root.val) # 再到中根遍历路径里找到根节点

            leftTreeInorder = inorder[: rootPosition] # 中根遍历路径中，根节点之前的元素全部属于左边子树
            rightTreeInorder = inorder[rootPosition + 1: ] # 中根遍历路径中，根节点之后到末尾的元素全部属于右边子树
            # 这样顺便知道了左边子树的节点总数，正好等于rootPosition，用这个节点总数信息，可以用来划分先根遍历路径
            leftTreePreorder = preorder[1: 1 + rootPosition] # 从第二个元素开始，数rootPosition个元素，属于左边子树
            rightTreePreorder = preorder[rootPosition + 1: ] # 左边子树之后全部是右边子树

            root.left = self.buildTree(leftTreePreorder, leftTreeInorder) # 用左边子树的先根遍历路径、中根遍历路径，继续确定左边子树的结构
            root.right = self.buildTree(rightTreePreorder, rightTreeInorder) # 用右边子树的先根遍历路径、中根遍历路径，继续确定右边子树的结构
            return root
        else:
            return None