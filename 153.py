from typing import *
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]
        return nums[0]

s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
