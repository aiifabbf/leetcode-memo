# 判断数组是否含有一个长度至少为2的substring（连续的）使得这个substring的加和等于k的某个倍数。

from typing import *

import collections
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        # left = 0
        # while left <= len(nums) - 2:
        #     right = left + 2
        #     summation = sum(nums[left: right])
        #     while right <= len(nums):
        #         # print(left, right)
        #         # summation = sum(nums[left: right]) # 每次都重新算有点慢了
        #         if k == 0 and summation == 0:
        #             return True
        #         elif k != 0 and summation % k == 0:
        #             return True
        #         right += 1
        #         summation += sum(nums[right-1: right])
        #     left += 1
        
        # return False
        # 一改：O(n^2)也太慢了……
        


s = Solution()
assert s.checkSubarraySum([23, 2, 4, 6, 7], 6)
assert s.checkSubarraySum([23, 2, 6, 4, 7], 6)
assert not s.checkSubarraySum([23, 2, 6, 4, 7], 0)
assert s.checkSubarraySum([0, 0], 0)
assert not s.checkSubarraySum([0, 1, 0], 0)