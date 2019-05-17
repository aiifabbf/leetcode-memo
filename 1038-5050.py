"""
把一个二分搜索树变成一个所谓的最大搜索树。

这个最大搜索树其实就是逆中根遍历（先右边子树、然后当前节点、再左边子树）、求累加和构造出来的。所以我的做法就很暴力

1.  中根遍历原树，得到原树的中根遍历路径
2.  颠倒一下原树的中根遍历路径
3.  用 ``itertools.accumulate()`` 求累加和
4.  再颠倒一下

此时的路径就是所谓最大搜索树的中根遍历路径。按照这个路径把原树的每个节点依次修改成新的节点值就好了。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import itertools

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            array = self.inorderTraversal(root) # 为了能重用中根遍历的代码，这里是常规的中根遍历
            array = list(reversed(list(itertools.accumulate(reversed(array))))) # 把中根遍历路径颠倒一下、再求累加和、再颠倒回来，这样操作之后，array就是所谓的最大和搜索树的中根遍历路径
            self.inorderModify(root, array) # 修改原树，变成所谓的最大和搜索树。这个函数有副作用，会不停pop掉array的第一个元素
            return root
        else:
            return None

    def inorderTraversal(self, root: TreeNode) -> List[int]: # 正常的中根遍历
        if root:
            res = []
            if root.left:
                res += self.inorderTraversal(root.left)
            res.append(root.val)
            if root.right:
                res += self.inorderTraversal(root.right)
            return res
        else:
            return []

    def inorderModify(self, root: TreeNode, array: List[int]) -> None: # 中跟修改，递归地把array的第一个元素设置成当前节点的值
        if root:
            if root.left:
                self.inorderModify(root.left, array)
            root.val = array.pop(0) # 副作用，会修改array
            if root.right:
                self.inorderModify(root.right, array)
        else:
            pass