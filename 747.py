"""
如果array里面最大的数字比其他数字都至少大两倍，就返回这个最大数字的下标；否则返回-1。
"""

from typing import *

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # maximum = 0
        # maximumPosition = -1
        # secondMaximum = 0

        # for i, v in enumerate(nums):
        #     if v >= maximum:
        #         secondMaximum = maximum
        #         maximum = v
        #         maximumPosition = i
        #     elif secondMaximum <= v < maximum:
        #         secondMaximum = v
        # 遍历一遍的做法。同时记录最大值、最大值的位置和第二大的值。
        
        # if maximum >= 2 * secondMaximum:
        #     return maximumPosition
        # else:
        #     return -1
        # 一改：做的有点复杂了……但是如果是C的话应该就这么写吧……

        # maximum = max(nums)
        # if any(maximum < 2 * i for i in nums if i != maximum):
        #     return -1
        # else:
        #     return nums.index(maximum)
        # # 不可思议啊，这个明明要遍历3遍，居然比我上面遍历1遍的快。

        maximum = -1
        maximumPosition = -1

        for i, v in enumerate(nums):
            if v >= maximum:
                maximum = v
                maximumPosition = i
        
        for i, v in enumerate(nums):
            if v != maximum:
                if v * 2 > maximum:
                    return -1
        
        return maximumPosition