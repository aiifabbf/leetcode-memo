"""
找到一个二叉树里所有相等的子树。树相等需要两点

-   结构完全相同
-   每个节点的值完全相同

所以可以找一种方法，把树做一个序列化，变成类似hash code的东西，这个hash code可以唯一地确定一个树，并且如果两个树的hash code相同，说明两个树相等。

在遍历的过程中，每次遇到一个子树就先序列化得到hash code，再到Counter/HashMap里看以前有没有见过，如果发现见过，就放到结果里。

.. note::

    注意题目明确说了，相同的子树在结果里只要出现一次就可以，意思是如果一个子树反反复复出现了三遍，在结果里也只要出现一次就可以了，所以判断的标准是以前见过且仅见过一次。

所以关键问题就是怎样选取一种hash code，又快占用空间又小。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools
import collections

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if root:
            counter = collections.Counter()
            res = []
            queue = [root]

            while queue:
                levelQueue = []

                for i in queue:
                    hashCode = self.hashTree(i)
                    counter[hashCode] += 1
                    if counter[hashCode] == 2:
                        res.append(i)

                    if i.left:
                        levelQueue.append(i.left)
                    if i.right:
                        levelQueue.append(i.right)

                queue = levelQueue

            return res
        else:
            return []

    @functools.lru_cache()
    def hashTree(self, root: TreeNode) -> tuple:
        if root:
            res = (root.val, )
            res += (self.hashTree(root.left), )
            res += (self.hashTree(root.right), )
            return res
        else:
            return tuple()