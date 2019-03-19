"""
判断两个二叉树是否是 **翻转相等** 的。

所谓翻转相等的意思是，树1通过任意次翻转 [#]_ 其中的任意一个子树能够得到树2。

.. [#] 翻转的意思 **不是** 左右镜面一下（沿y轴镜面对称一下），而是左边子树和右边子树交换位置，就是左边子树变成右边子树、同时右边子树变成左边子树。226题才是镜面的意思。著名的homebrew作者翻车题。(每次说到这道题都要鞭尸一下是不是不太好……)

我想到了两种做法

-   先得到根节点到所有叶子的所有路径集合，对比这两个集合是否完全相等

    显然调换左右边子树是不会让根节点到任意一个叶子的路径出现变化的。

-   递归地测试

    -   树1的左边子树、和树2的右边子树是否翻转相等
    -   树1的左边子树、和树2的左边子树是否翻转相等

    两个条件只要满足一个就可以了。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        return set(self.routeFromRootToLeaves(root1)) == set(self.routeFromRootToLeaves(root2))
        
    def routeFromRootToLeaves(self, root: TreeNode) -> List[int]:
        if root:
            if root.left == None and root.right == None:
                return [
                    (root.val, )
                ]
            else:
                return [
                    (root.val, ) + i for i in self.routeFromRootToLeaves(root.left) + self.routeFromRootToLeaves(root.right)
                ]
        else:
            return []