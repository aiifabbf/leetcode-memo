"""
一个从小到大排好序的array偏移了几个元素，要你在 :math:`O(\ln n)` 复杂度里找到某个元素的下标。
"""

from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums:
            sentinel = None
            head = nums[0]
            previous = sentinel
            i = 0

            while True:
                if nums[i] == target:
                    return i
                if 
        else:
            return -1