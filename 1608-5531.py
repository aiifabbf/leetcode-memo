"""
.. default-role:: math

给一个array，是否存在一个自然数 `n` 使得array里面恰好存在 `n` 个大于等于 `n` 的数字？

先看下 `n` 可能的范围是什么，假设array的长度是 `m` ，既然 `n` 是array里有多少个满足什么什么条件的元素的个数，那么 `n` 的范围只可能是 `[0, m]` 。那就一个一个试咯。
"""

from typing import *

import bisect


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums) # 先从小到大排序，这样如果找到一个数字k，k后面所有的数字都大于等于k

        for i in range(0, len(nums) + 1): # n的范围是[0, len(array)]，一个一个试
            index = bisect.bisect_left(nums, i) # 用二分，找到第一个大于等于n的数字
            if len(nums) - index == i: # 这个数字和后面所有的数字都是大于等于n的，假设这个数字下标是i，那么总共有len(array) - i个大于等于n的数字
                return i

        return -1


s = Solution()
print(s.specialArray([3, 5])) # 2
print(s.specialArray([0, 0])) # -1
print(s.specialArray([0, 4, 3, 0, 4])) # 3
print(s.specialArray([3, 6, 7, 7, 0])) # -1
