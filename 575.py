"""
长度为偶数的array中的每个元素的数字都代表某种糖果的牌子，这个数字出现的次数代表有多少个这个牌子的糖果，现在要把这个array分成两个长度相等的subsequence，使得其中一个subsequence含的牌子种类最多。问这个subsequence里最多能有多少种牌子。

.. 真的好绕口啊……
"""

from typing import *

# import collections

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        # counter = collections.Counter(candies) # 遇到这种次数的题目，二话不说就用Counter先来一波
        # return min(len(candies) // 2, len(counter))
        # 后来发现counter好像没发挥什么作用……好像就发挥了一个set的作用，那索性改成set
        return min(len(candies) // 2, len(set(candies)))

# s = Solution()
# print(s.distributeCandies([1, 1, 2, 2, 3, 3,]))
# print(s.distributeCandies([1, 1, 2, 3]))
# print(s.distributeCandies([1, 1, 1, 1, 1, 1]))