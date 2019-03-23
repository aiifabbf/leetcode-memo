"""
给一个array，它的所有长度为k的substring（连续）的最大平均值是多少？
"""

from typing import *

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = float("-inf")
        summation = sum(nums[0: k]) # 优化一下，不用每次都重新算

        for i in range(len(nums) - k):
            maximum = max(maximum, summation / k)
            summation -= nums[i]
            summation += nums[i + k]

        maximum = max(maximum, summation / k) # 最后终止还要再算一下
        
        return maximum