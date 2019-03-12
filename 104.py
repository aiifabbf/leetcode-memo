# 输出一个二叉树的最大深度

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root: # 确定存在根节点
            depth = 1 # 保存已知深度。因为现在已经确定存在根节点，所以已知深度是1
            queue = [root]
            while queue:
                levelQueue = []
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)
                depth += 1
                queue = levelQueue
            return depth - 1
        else:
            return 0