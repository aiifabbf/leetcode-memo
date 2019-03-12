# 输出一个二叉树每一层节点的平均值

# 那……又是广度优先搜索了吧

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root:
            res = []
            queue = [root]
            while queue:
                levelQueue = []
                for i in queue:
                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)

                res.append(sum(i.val for i in queue) / len(queue))
                queue = levelQueue
            return res
        else:
            return []

# 最快的代码好像和我的一样啊……