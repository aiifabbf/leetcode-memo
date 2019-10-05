"""
取三个从小到大排好序的array的共同的交集

应该是能利用一下性质的，但我懒。
"""

from typing import *

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(set(arr1).intersection(arr2).intersection(arr3))

# s = Solution()
# print(s.arraysIntersection([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]))