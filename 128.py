"""
从array中可以最多挑多少个元素出来，能形成一个最长的公差为1的等差数列？

暴力做法就是一个一个元素地遍历，然后不停地查找比这个元素大1的元素是否在array里面。

这里有两个地方可以优化

-   因为是挑元素，所以与元素在array中的顺序其实无关（array的任何一种排列都应该得到同样的结果）

    所以这里的array可以退化成set，这样判断某个元素是否在array里的复杂度可以降低到 :math:`O(1)`

-   遍历元素的时候，如果这个元素不是某个等差数列最小的那个元素，会出现重复查找

    所以在遍历到一个元素的时候，可以先看一下比这个元素小1的元素是否在array里面，如果在array里面，说明当前元素不是等差数列里最小的那个元素，也许之前已经搜索过了，或者之后会遇到那个最小的元素，不管怎样，当前也就没必要白费力气去往后搜索了。
"""

from typing import *

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            numberSet = set(nums)
            res = 1

            for number in numberSet:
                if number - 1 not in numberSet: # 确定当前元素已经是能形成某个等差数列的最小的元素了
                    longestConsecutiveArrayLengthStartingFromHere = 1 # 单元素也可以形成等差数列

                    while number + 1 in numberSet: # 比根元素大1的元素也在array里面
                        longestConsecutiveArrayLengthStartingFromHere += 1
                        number = number + 1
                    
                    res = max(res, longestConsecutiveArrayLengthStartingFromHere)
                else: # 如果不是等差数列的根元素，那么后面会遍历到的，所以这里就不用白费力气了
                    pass

            return res
        else:
            return 0

# s = Solution()
# assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4