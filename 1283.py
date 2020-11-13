"""
.. default-role:: math

给个array，找到一个数字 `k` ，使得array里面每个数字 `a_i` 除以 `k` 并且向上取整之后的累加和 `\sum_{a_i} \lceil a_i / k \rceil` 小于等于 `t` 。

详细解释在Rust写的版本里。大致思路是归约到判定表述、再用二分找到满足判定的最小取值。
"""

from typing import *

import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def feasible(divisor: int) -> bool:
            # 被除数是divisor的时候，能不能满足条件
            # 观察到，如果被除数是10的时候能满足条件，那么被除数是11的时候也能满足条件
            return sum(math.ceil(v / divisor) for v in nums) <= threshold

        # 俗套的二分
        target = True
        left = 1
        right = 2 * max(nums) + 1

        while left < right:
            middle = (left + right) // 2
            test = feasible(middle)
            if target < test:
                right = middle
            elif target > test:
                left = middle + 1
            else:
                right = middle

        return left