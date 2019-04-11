"""
找到array里极大值点的下标

挺简单的， :math:`O(n)` 扫描一遍。
"""

from typing import *

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float("-inf")] + nums + [float("-inf")] # 两边加个负无穷，省得烦

        for i, v in enumerate(nums[1: -1], 1):
            if nums[i - 1] < v > nums[i + 1]:
                return i - 1 # 记得负无穷要去掉，所以下标-1
        else:
            return -1