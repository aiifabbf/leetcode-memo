"""
在array里找到一个数，这个数的左边所有的元素加起来的和等于这个数的右边所有的元素加起来的和。如果不存在，就返回-1。

挺简单的，这道题的重点就是左边右边的sum不能每次都重新算，这样一定能过。
"""

from typing import *

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if nums:
            summation = sum(nums)
            leftSummation = 0 # 当然不能每次都重新算，太慢了
            rightSummation = summation

            for i, v in enumerate(nums):
                rightSummation -= v
                if leftSummation == rightSummation:
                    return i
                leftSummation += v
            else:
                return -1

        else:
            return -1