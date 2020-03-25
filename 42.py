"""
.. default-role:: math

接雨水

Rust版里有详细解释。简单讲讲就是搞2个cumulative maximum，一个是第 `i` 个元素前的最大值，一个是第 `i` 个元素往后的最大值。
"""

from typing import *


class Solution:
    def trap(self, height: List[int]) -> int:
        cumulativeMaximumBefore = [0] # cumulativeMaximumBefore[i]是height[: i]里的最大值
        cumulativeMaximumAfter = [0] # cumulativeMaximumAfter[i]是height[i: ]里的最大值

        for v in height:
            cumulativeMaximumBefore.append(max(v, cumulativeMaximumBefore[-1]))

        for v in reversed(height):
            cumulativeMaximumAfter.append(max(v, cumulativeMaximumAfter[-1]))

        cumulativeMaximumAfter.reverse()

        res = 0

        for i, v in enumerate(height):
            sideHeight = min(
                cumulativeMaximumBefore[i], cumulativeMaximumAfter[i + 1])
            if v < sideHeight:
                res += sideHeight - v

        return res


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
