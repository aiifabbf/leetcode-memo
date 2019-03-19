"""
在一个含重复元素的二分搜索树 [#]_ 里找到出现频次最高的元素。

.. [#] 含重复元素的二分搜索树里面，可以保证左边子树里的每一个节点值都 **小于等于** 根节点的值，右边子树里的每一个节点值都 **大于等于** 根节点的值。

可以当初普通的二叉树来做，也就是和508题一模一样的做法。但是既然这道题给了二分搜索树，说明可能要想办法利用二分搜索树的性质来加速。

.. 但我不管这么多了……

.. 好的，暴力做是会超时的。24/25个case是一个超大的二叉树。

.. 好的，暴力做是不会超时的，因为最耗时间的步骤不是遍历，而是Counter求频次最高的项。
"""

from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root:
            queue = [root]
            counter = collections.Counter()

            while queue:
                i = queue.pop()
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
                counter[i.val] += 1

            maximumFrequency = counter.most_common(1)[0][1] # 这里坑了。千万不要图省力，把这个求最大频次的语句放到下面的list comprehension里，因为每次都会重新算……
            return [i for i, v in counter.items() if v == maximumFrequency]
        else:
            return []