"""
原地（in-place）合并两个已经从小到大排好序的array。

这个操作会出现在merge sort算法里面。
"""

from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[:] = sorted(nums1 + nums2) # 这样不太好吧

        a = nums1[0: m]
        b = nums2[0: n]
        res = []

        while a and b:
            if a[0] <= b[0]:
                res.append(a.pop(0))
            else:
                res.append(b.pop(0))
        
        if a:
            res += a
        else:
            res += b

        nums1[:] = res