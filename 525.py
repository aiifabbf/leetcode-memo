r"""
.. default-role:: math

给一个array，问其中含有相等数量的0和1的substring（要连续）的最大长度是多少。

.. 想了一分钟就想到了，真爽啊。

先把array里面所有的0都变成-1，这样如果某个substring里原来有相同数量的0和1的话，这个substring的累加和就是0。

划重点，累加和。遇到这个东西，马上就要想到积分。假设把0全部变成1之后，array是 ``a[i]`` ，积分之后 ``b[i]`` ，那么问题转换成找到所有 `(i, j), i < j` ，使得 `b_i = b_j` ，并且返回其中最大的 `j - i` ，就是找到

.. math::

    \max\{j - i | b_i = b_j, 0 \leq i < j \leq n - 1\}

所以这里有两个需求

-   遍历到 `b_j` 的时候，需要快速知道前面是否存在一个 `b_i = b_j`
-   如果前面存在一个 `b_i = b_j` ，需要快速知道它的下标 `i`

所以这里用一个 ``dict`` 来存前面遇到过的积分值，key是积分值，value是积分值所在的下标。

因为需要最大化 `j - i` ，所以遇到 `b_i = b_j` 的时候，不要更新 ``dict[b[j]]`` ，保持第一次遇到的value。如果不存在 `b_i = b_j` ，才添加 ``dict[b[j]] = j` 这条记录。
"""

from typing import *

import itertools

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        array = (v if v == 1 else -1 for v in nums) # 用generator省内存、省时间
        integrals = itertools.chain([0], itertools.accumulate(array)) # 用chain连接两个iterator
        seen = {} # key是积分值，value是第一次遇到这个积分值的时候的下标
        res = 0 # 目前最大的j - i

        for i, v in enumerate(integrals): # 遍历积分值
            if v in seen: # 如果积分值在前面遇到过
                res = max(res, i - seen[v]) # 更新j - i的最大值
            else: # 没有遇到过
                seen[v] = i # 添加记录

        return res

# s = Solution()
# print(s.findMaxLength([0, 1])) # 2
# print(s.findMaxLength([0, 1, 0])) # 2