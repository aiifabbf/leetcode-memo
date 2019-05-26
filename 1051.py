"""
为了使一个array变成从小到大排好序的array，最少需要交换多少个元素的位置？

做法很简单，直接给这个array排序就好、然后做个diff、统计总共有多少个元素不在同一个位置。
"""

from typing import *

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights) # 排序
        return sum((True if heights[i] != sortedHeights[i] else False for i in range(len(heights)))) # 做diff

# s = Solution()
# print(s.heightChecker([1, 1, 4, 2, 1, 3])) # 3