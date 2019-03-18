"""
找到二叉树里，路径和为sum的所有单向向下的路径。

和113题的不同在于，113题要求路径必须从根节点出发、到达某个叶子节点，但是这一题没有要求这一点，只要求这条路径必须是单向向下的，意思是不能出现从一个节点出发向parent的方向。 [#]_

.. [#] 但是题目没说路径上只有一个节点算不算……

所以和113题不同的地方是

-   不一定非要到叶子
-   不能到一个节点就无脑 ``sum - node.val`` ，而是也要考虑sum
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            if root.left == None and root.right == None: # 叶子
                if root.val == sum:
                    return 1
                else:
                    return 0
            else: # 不是叶子
                if root.val == sum: # 到这个节点为止已经存在路径了
                    return 1 + self.pathSum(root.left, sum) + self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum) + self.pathSum(root.right, sum - root.val)
                else: # 到这个节点为止还不存在路径
                    return self.pathSum(root.left, sum) + self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum) + self.pathSum(root.right, sum - root.val)
        else:
            return 0