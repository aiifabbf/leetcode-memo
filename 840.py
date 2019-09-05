"""
给一个矩阵，问这个矩阵有多少个3x3的子矩阵可以做到

-   每行、每列、主对角线、副对角线的和相等
-   子矩阵里的元素正好是1-9

看题目的要求，矩阵的长、宽不超过10，所以直接暴力做就好了。
"""

from typing import *

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        columnCount = len(grid[0])
        res = 0

        for rowIndex in range(rowCount - 3 + 1):

            for columnIndex in range(columnCount - 3 + 1):
                subgrid = [
                    grid[rowIndex + r][columnIndex + c]
                    for r in range(3)
                    for c in range(3)
                ]
                if set(subgrid) == set(range(1, 10)) and subgrid[0] + subgrid[1] + subgrid[2] == subgrid[3 + 0] + subgrid[3 + 1] + subgrid[3 + 2] == subgrid[6 + 0] + subgrid[6 + 1] + subgrid[6 + 2] == subgrid[0] + subgrid[3 + 0] + subgrid[6 + 0] == subgrid[1] + subgrid[3 + 1] + subgrid[6 + 1] == subgrid[2] + subgrid[3 + 2] + subgrid[6 + 2] == subgrid[0] + subgrid[3 + 1] + subgrid[6 + 2] == subgrid[2] + subgrid[3 + 1] + subgrid[6 + 0]: # 每行、每列、主对角线、副对角线的和一致
                    res += 1

        return res

# s = Solution()
# print(s.numMagicSquaresInside([
#     [4, 3, 8, 4], 
#     [9, 5, 1, 9], 
#     [2, 7, 6, 2]
# ])) # 1
# print(s.numMagicSquaresInside([
#     [3, 2, 1, 6], 
#     [5, 9, 6, 8], 
#     [1, 5, 1, 2], 
#     [3, 7, 3, 4]
# ]))
# print(s.numMagicSquaresInside([
#     [8, 1, 6],
#     [3, 5, 7],
#     [4, 9, 2]
# ]))