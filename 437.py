"""
找到二叉树里，路径和为sum的所有单向向下的路径。

和113题的不同在于，113题要求路径必须从根节点出发、到达某个叶子节点，但是这一题没有要求这一点，只要求这条路径必须是单向向下的，意思是不能出现从一个节点出发向parent的方向。 [#]_

.. [#] 但是题目没说路径上只有一个节点算不算……

所以和113题不同的地方是

-   不一定非要到叶子
-   不能到一个节点就无脑 ``sum - node.val`` ，而是也要考虑sum

.. 这道题隔了几天才做出来的。受了687题和543题的启发，每次遇到这种类似 **没规定一定要从根节点出发的路径** 的题目，都是先假定只能从根路径出发，然后遍历树里的节点、对树里面每一个子树都算出一个只能从子树根节点出发的路径。

.. 写到这里突然又想到那道股票dp的题目……怎么说呢，两道题有异曲同工之妙，都是没有限定从哪里出发，所以一开始就很难，但是如果你限定一下从一个位置出发，然后对每个可能的位置都做一次操作，就完成了。
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
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            queue = [root]
            count = 0

            while queue: # 遍历每个子树
                i = queue.pop(0)
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
                count += self.pathSumCount(i, sum)

            return count
        else:
            return 0

    @functools.lru_cache()
    def pathSumCount(self, root: TreeNode, sum: int) -> int: # 从根节点出发，向下能加到sum的路径的数量
        if root:
            if root.left == None and root.right == None: # 叶子
                if root.val == sum:
                    return 1
                else:
                    return 0
            else: # 不是叶子
                if root.val == sum: # 到这个节点为止已经存在路径了
                    return 1 + self.pathSumCount(root.left, sum - root.val) + self.pathSumCount(root.right, sum - root.val) # 但是不代表直接不用搜索下去了，试想如果有节点的值是0呢？
                else: # 到这个节点为止还不存在路径
                    return 0 + self.pathSumCount(root.left, sum - root.val) + self.pathSumCount(root.right, sum - root.val) # 这里我人晕了……函数名记得一定要检查啊
        else:
            return 0