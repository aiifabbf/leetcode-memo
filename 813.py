"""
把一个array最多分为K个substring（连续），问这些substring的平均值之和最大值是多少。
"""

from typing import *

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        