"""
找到一个array中最长的锯齿状subsequence（不一定要连续）的长度

看到这道题就有一种978题的感觉，那一题是要求最长的锯齿状的substring，这一题是subsequence。

应该也是dp。设 :math:`p_i` 是以第i个元素为结尾的最长锯齿状subsequence的长度。那么 :math:`p_i` 和前面的项的关系就没有substring那个那么简单了，需要一个额外的信息来确定以第i个元素为结尾的锯齿状subsequence最后的走向是向上、向下、还是平 [#]_ 。

.. [#] 假设这个锯齿状subsequence只有一个元素，就会出现无法确定走向的情况。

因为是subsequence， :math:`O(n^2)` 应该是正常做法的复杂度……我想不出 :math:`O(n)` 的做法。
"""

from typing import *

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            dp = [
                (1, None) # 第一个元素记录以第i个元素为结尾的最长锯齿状subsequence的长度，第二个元素记录到第i个元素前的走向。这里因为是第一个元素，所以走向不明。
            ]
            maximumLength = 1 # 一边dp一边记录最长长度，省得最后再遍历

            for i, v in enumerate(nums[1: ], 1):
                maximumLengthEndingHere = 1 # 以第i个元素为结尾的最长锯齿状subsequence的长度
                upward = None # 最后的走向

                for index, (longestLength, goingUp) in enumerate(dp):
                    # if goingUp == True and v < nums[index]: # 这个元素走向是向上，下一个应该向下
                    #     maximumLengthEndingHere = max(maximumLengthEndingHere, longestLength + 1)
                    #     upward = False
                    # elif goingUp == False and v > nums[index]: # 这个元素走向是向下，下一个应该向上
                    #     maximumLengthEndingHere = max(maximumLengthEndingHere, longestLength + 1)
                    #     upward = True
                    # elif goingUp == None and v < nums[index]: # 走向不明，依照和上一个元素的关系来确定当前走向
                    #     maximumLengthEndingHere = max(maximumLengthEndingHere, longestLength + 1)
                    #     upward = False
                    # elif goingUp == None and v > nums[index]: # 走向不明，依照和上一个元素的关系来确定当前走向
                    #     maximumLengthEndingHere = max(maximumLengthEndingHere, longestLength + 1)
                    #     upward = True
                    # else:
                    #     pass
                    # 一改：简化if流程。虽然可读性没以前那么强了，但是速度提升还是挺大的
                    if v < nums[index]:
                        if goingUp != False:
                            maximumLengthEndingHere = max(maximumLengthEndingHere, longestLength + 1)
                            upward = False
                    elif v > nums[index]:
                        if goingUp != True:
                            maximumLengthEndingHere = max(maximumLengthEndingHere, longestLength + 1)
                            upward = True

                maximumLength = max(maximumLengthEndingHere, maximumLength)
                dp.append((maximumLengthEndingHere, upward))

            return maximumLength

# s = Solution()
# assert s.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
# assert s.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
# assert s.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
# assert s.wiggleMaxLength([]) == 0
# assert s.wiggleMaxLength([1]) == 1
# assert s.wiggleMaxLength([1, 2]) == 2