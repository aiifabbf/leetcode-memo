"""
数出一个完全二叉树里的节点的个数

随你怎么遍历都可以。但是既然题目说了是完全二叉树，应该可以有一些性质可以利用。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            count = 0

            while queue:
                i = queue.pop()
                count += 1
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            
            return count
        else:
            return 0

        # 优化再说吧……