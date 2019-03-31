"""
给一个array的一个子集（乱序subsequence）里的每个元素，找到它在原array里的位置右边开始第一个比它大的元素。

.. 先试了下暴力，结果居然过了……那就以后再说了……
"""

from typing import *

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for v in nums1:
            index = nums2.index(v) # 找到元素在原arrray中的位置，因为题目说确定存在，所以不用try block

            for i in range(index + 1, len(nums2)): # 从位置的右边开始找
                if nums2[i] > v: # 找到了
                    res.append(nums2[i])
                    break
            else: # 没找到
                res.append(-1)

        return res

# s = Solution()
# print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
# print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))