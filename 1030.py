"""
把一个矩阵里的所有格子按照和(r0, c0)的距离排序

不谈了，挺简单的一道题。
"""

from typing import *

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        
        for r in range(R):

            for c in range(C):
                res.append([r, c])

        return sorted(res, key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))

# s = Solution()
# assert s.allCellsDistOrder(1, 2, 0, 0) == [[0, 0], [0, 1]]
# assert s.allCellsDistOrder(2, 2, 0, 1) == [[0, 1], [0, 0], [1, 1], [1, 0]]