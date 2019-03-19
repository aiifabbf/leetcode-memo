"""
在一个二叉树里面，找到两个节点的最近公共祖先节点的值。

.. 有种似曾相识的感觉……因为235题里做过了。235题里面是在一个二分搜索树里找到两个节点的最近公共祖先节点，这道题是在一个普通的没什么特点的二叉树里找到两个节点的最近公共祖先节点。

.. 所以235题好像做错了，应该是有一些性质可以利用的。

.. 235题没做错……我确实利用了二分搜索树的性质，因为我在这里写寻找根节点到目标节点的路径的函数的时候卡住了。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import functools

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        routeToP = self.routeToNode(root, p.val)
        routeToQ = self.routeToNode(root, q.val)

        # 和235题一样，做一个diff
        for i in range(min(len(routeToP), len(routeToQ))):
            if routeToP[i].val != routeToQ[i].val:
                return routeToP[i - 1]
        else: # for循环顺利走完没有中途break。说明出现了包含关系
            return routeToP[i]

    @functools.lru_cache()
    def routeToNode(self, root: TreeNode, value: int) -> List[int]:
        if root:
            if root.val == value:
                return [root]
            else:
                res = [root]
                left = self.routeToNode(root.left, value)
                if left and left[-1].val == value:
                    return res + left
                right = self.routeToNode(root.right, value)
                if right and right[-1].val == value:
                    return res + right
                return res
        else:
            return []

    # 这也太慢了……