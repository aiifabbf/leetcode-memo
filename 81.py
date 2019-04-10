"""
递增array从中间断开，左半边移到右边去了，在 :math:`O(\ln n)` 复杂度里判断一个元素在不在array中。

和33题不同的地方在于原array里不再是严格递增的了，所以说可能会含有重复元素。

这时候有一个绝妙的办法是，刷一遍array，把重复的元素去掉，array中就不再含重复元素了，这个问题就转化成我们解决过的问题了。可是你有没有发现，刷一遍array的复杂度是 :math:`O(n)` ……还不如刷一遍直接找到target。
"""

from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # return target in nums # 万能方法
        if nums == []:
            return False

        res = [nums[0]]
        
        for i, v in enumerate(nums[1: ], 1):
            if v != nums[i - 1]:
                res.append(v)
            else:
                pass

        nums = res

        left = 0
        right = len(nums)
        if nums[0] >= nums[-1]:

            while left < right:
                middle = (left + right) // 2
                if middle - 1 >= 0:
                    if nums[middle - 1] > nums[middle]:
                        breakingPosition = middle
                        break
                else:
                    breakingPosition = 0
                    break

                if nums[middle] > nums[0]:
                    left = middle + 1
                else:
                    right = middle

        else:
            breakingPosition = 0

        if breakingPosition == 0:
            left = 0
            right = len(nums)
        else:
            if target >= nums[0]:
                left = 0
                right = breakingPosition
            else:
                left = breakingPosition
                right = len(nums)
        
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            else:
                return True

        return False

# s = Solution()
# assert s.search([1, 1, 1, 1,], 1) == True
# assert s.search([1, 1, 1, 1,], 2) == False
# assert s.search([2, 5, 6, 0, 0, 1, 2], 0) == True
# assert s.search([2, 5, 6, 0, 0, 1, 2], 3) == False
# assert s.search([2, 5, 6, 6, 7, 0, 1, 2, 2], 2) == True
# assert s.search([2, 5, 6, 6, 7, 0, 1, 2, 2], 7) == True
# assert s.search([2, 5, 6, 6, 7, 2, 2, 2, 2], 2) == True
# assert s.search([2, 2, 2, 2, 0, 1, 1, 1, 2, 2,], 2) == True
# assert s.search([2, 2, 2, 2, 0, 2, 2,], 2) == True
# assert s.search([2, 2, 2, 2, 0, 2, 2,], 0) == True
# assert s.search([2, 2, 2, 2, 2, 2, 2, 2, 2,], 2) == True
# assert s.search([1, 3], 0) == False