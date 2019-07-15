"""
二叉树中所有深度最大的叶子节点的最深公共祖先节点。

首先广度优先、按层遍历得到最下面一层的所有的叶子节点，然后再获得它们的最深公共祖先节点。

获得两个节点的最深公共祖先节点可以直接用 `236 <./236.py>`_ 的代码，因为这里可能需要找超过两个节点的最深公共祖先节点，这个函数满足结合律和交换律，所以再套一个reduce就好了。
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
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        queue = [root]

        while queue != []: # 广度优先
            levelQueue = [] # 按层遍历

            for v in queue:
                if v.left:
                    levelQueue.append(v.left)
                if v.right:
                    levelQueue.append(v.right)

            if levelQueue == []: # 发现下面一层没有节点了，说明这是最后一层了
                deepestLeaves = list(filter(lambda v: v.left == None and v.right == None, queue)) # 得到最深的叶子
                break
            else:
                queue = levelQueue

        return functools.reduce(lambda v, w: self.lowestCommonAncestor(root, v, w), deepestLeaves) # 得到这些最深叶子共同的最深公共祖先节点

    # 摘自236
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