"""
array中有多少对 :math:`\{a_i, a_j\}, i \neq j, |a_i - a_j| = k` ？不考虑顺序。

这道题出的挺无聊的，因为主要就考察你有没有忽略 ``k == 0`` 的情况，如果 ``k == 0`` ，不是说array有多少个元素就有多少对，因此题目还隐含了，这个对子里的两个数，不能有相同的下标，也就是不能自己和自己成对。

又被坑了…… ``k < 0`` 的话就直接返回0，因为绝对不可能有哪两个数的差的绝对值是负数的。
"""

from typing import *

import collections

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        summation = 0

        if k == 0:
            return sum(1 for v, c in counter.items() if c > 1) # 不能和自身成对
        elif k > 0:
            return sum(1 for v, c in counter.items() if v + k in counter) # 只要数一次，因为不考虑顺序
        else:
            return 0