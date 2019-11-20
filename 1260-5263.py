"""
先把一个矩阵展平，然后让其中的元素往前循环位移 `k` 格。

比如

::

    1 2 3
    4 5 6
    7 8 9

往前循环2格变成

::

    8 9 1
    2 3 4
    5 6 7

没什么好说的，就展平、循环、再整回原来的shape就好了。
"""

from typing import *

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rowCount = len(grid) # 原来矩阵的行数
        columnCount = len(grid[0]) # 原来矩阵的列数
        flattened = self.flatten(grid) # 把矩阵展平
        k = k % len(flattened) # 向前循环位移k格和向前循环位移“k对矩阵展平之后的长度取余数”格是一样的效果
        flattened = flattened[-k: ] + flattened[: -k] # 向前循环位移k格
        res = []

        for rowIndex in range(rowCount): # 再从展平的一维向量恢复回来
            res.append([flattened[rowIndex * columnCount + i] for i in range(columnCount)])

        return res

        # 如果用numpy的话更简单

    def flatten(self, matrix: List[List[int]]) -> List[int]: # 展平矩阵
        return sum(matrix, []) # 就是把每一行都连接起来

# s = Solution()
# print(s.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
# print(s.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
# print(s.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))
# print(s.shiftGrid([[1],[2],[3],[4],[7],[6],[5]], 23))