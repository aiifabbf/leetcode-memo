"""
"""

from typing import *

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # S = []
        maxLength = float("-inf")

        for i, v in enumerate(nums):
            seen = set()
            tempS = []

            while True:
                if nums[i] in seen:
                    break
                else:
                    tempS.append(nums[i])
                    seen.add(nums[i])
                    i = nums[i]
                
            maxLength = max(maxLength, len(tempS))

        # return max(map(len, S))
        return maxLength

s = Solution()
# print(s.arrayNesting([5, 4, 0, 3, 1, 6, 2]))