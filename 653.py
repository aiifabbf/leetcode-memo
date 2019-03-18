"""
经典two sum，不过这次输入是一个二分搜索树。

当然不管是不是二分搜索树，总是退化成普通二叉树，再用遍历和HashSet方法解。但是这里既然说了是二分搜索树，是不是可以用一下二分搜索树的什么性质，省略掉一些没意义的搜索，让搜索变得更快。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root:
            records = set()
            queue = [root]
            levelQueue = []

            while queue:
                levelQueue.clear()

                for i in queue:
                    if - (k / 2 - i.val) in records:
                        return True
                    else:
                        records.add(k / 2 - i.val)
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)

                queue[:] = levelQueue

            return False
        else:
            return False

        # 针对BST优化的再说吧……