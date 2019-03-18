"""
找到最常出现的子树和。

所谓子树和就是一个子树里所有的节点的值加起来。
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import functools
import collections

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        counter = collections.Counter()
        queue = [root]

        while queue:
            i = queue.pop()
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
            counter[self.treeSum(i)] += 1

        # 下面的步骤其实挺麻烦的，就是要筛选出频次最高的，但是问题是可能会有多个元素频次一样多而且恰好是最高的。好像已经出现过很多次这种要求了，我也不知道最佳做法是什么。
        # res = []
        # maximumFrequency = counter.most_common(1)[0][1]

        # for index, value in counter.most_common():
        #     if value < maximumFrequency:
        #         return res
        #     else:
        #         res.append(index)
        
        # return res

        # 最佳做法知道了。https://leetcode.com/problems/most-frequent-subtree-sum/discuss/98675/Python-easy-understand-solution

        maximumFrequency = counter.most_common(1)[0][1]
        return [i for i, v in counter.items() if v == maximumFrequency]

    @functools.lru_cache()        
    def treeSum(self, root: TreeNode) -> int:
        if root:
            return root.val + self.treeSum(root.left) + self.treeSum(root.right)
        else:
            return 0