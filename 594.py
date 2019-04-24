"""
找到最长的harmonious subsequence（不一定连续）的长度。

所谓harmonious序列就是这个序列的最大值和最小值差值正好是1。

因为是subsequence，没有要求连续，所以我马上就想到了用Counter来做，先给array做一个直方图，然后遍历每个出现过的元素n，判断n+1是否出现过，如果出现过，那么可以构成一个harmonious序列；如果没出现过，那么不能构成harmonious序列。
"""

from typing import *

import collections

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = collections.Counter(nums) # 做一个直方图
        return max((counter[n] + counter[n + 1] for n in counter if n + 1 in counter), default=0) # 遍历每个出现过的元素n，看n+1有没有出现过，如果出现过，说明可以构成harmonious序列