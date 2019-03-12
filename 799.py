# 未完
from typing import *

import math
class Solution:
    """
    首先算出能使得 :math:`1 + 2 + \ldots + n \leq p` 的最大的 :math:`n`。
    """
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        bottomFullLevel = math.floor((-1 + math.sqrt(1 + 8 * poured)) / 2) - 1
        if query_row <= bottomFullLevel: # 全满
            return 1.0
        elif query_row - bottomFullLevel == 1: # 全满紧接着的下一层
            n = bottomFullLevel + 1
            remainingWine = poured - 1 / 2 * n * (n + 1)
            if query_glass == 0 or query_glass == bottomFullLevel:
                return remainingWine / 2 / bottomFullLevel
            else:
                return remainingWine / bottomFullLevel
        else: # 全空
            return 0.0

s = Solution()
print(s.champagneTower(1, 1, 1,))
print(s.champagneTower(2, 1, 1,))