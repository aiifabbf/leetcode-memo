"""
.. default-role:: math

给一个数组，每两个数 `a_{2k}, a_{2k + 1}` 代表原数组里有 `a_{2k}` 个 `a_{2k + 1}` 。还原出原数组。

很简单嘛，就按题目意思来做，两个两个遍历数组，然后把 `a_{2k}` 个 `a_{2k + 1}` 追加到原数组里面。
"""

from typing import *

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = [] # 还原出的原数组

        for i in range(0, len(nums) // 2): # 两个两个遍历数组
            a = nums[2 * i] # a个b
            b = nums[2 * i + 1] # a个b
            res.extend([b] * a) # 在原数组里添加a个b

        return res