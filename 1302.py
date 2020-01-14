"""
计算最深的叶子节点的值的和。

所谓最深就是最低层。

按层遍历就好了，把每层的和都加上，最后退出的时候就是最后一层所有节点的和。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            res = 0

            while queue: # 按层遍历
                size = len(queue)
                res = 0

                for _ in range(size):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    res += node.val # 把这一层所有的节点的和加起来

            return res # res是退出while前那一层的所有节点的和、也就是最后一层所有节点和
        else:
            return 0