# 找到点集中满足 :math:`|j - i| = |k - i|` 的点对 :math:`(i, j, k)` 的个数

from typing import *

import collections
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangsCount = 0
        counter = collections.Counter()
        for p in points:
            counter.clear() # 这样重复用一个counter应该会快很多……好吧没有快很多
            for q in points:
                counter[(q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2] += 1

            for key, value in counter.items():
                boomerangsCount += value * (value - 1)

        return boomerangsCount

s = Solution()
assert s.numberOfBoomerangs([[0,0],[1,0],[2,0]]) == 2