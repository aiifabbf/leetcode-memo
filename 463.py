"""
给一个二维矩阵，1表示陆地、0表示海水，矩阵里只有一个岛屿，问这个岛屿的边长是多少

比如给一个

::

    0, 0, 1, 0, 0
    0, 0, 1, 0, 0
    0, 1, 1, 1, 0

边长是12。

很简单，找下规律，对于一块陆地，如果它周围4个方块都是陆地的话，那么这块陆地在内陆，并不贡献边长；如果周围4个方块有3个都是陆地、1是海水的话，那么这块陆地贡献1单位的边长。

所以很显然，如果一块陆地的周围有 `i` 个海水，那么这个陆地就贡献 `i` 个单位的边长。遍历一遍，找到所有陆地，再把这些陆地贡献的边长都加起来，就是整个岛屿的边长了。

如果陆地正好在边界上，边界也看做是海水。
"""

from typing import *


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        columnCount = len(grid[0])
        res = 0

        for rowIndex, row in enumerate(grid):

            for columnIndex, box in enumerate(row):
                if box == 1:
                    neighbors = [
                        (rowIndex - 1, columnIndex),
                        (rowIndex + 1, columnIndex),
                        (rowIndex, columnIndex - 1),
                        (rowIndex, columnIndex + 1),
                    ] # 上下左右四个邻居

                    for neighbor in neighbors:
                        if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount:
                            if grid[neighbor[0]][neighbor[1]] == 0: # 这个邻居是海水
                                res += 1 # 所以贡献了一个单位的边长
                        else: # 如果这块陆地正好在边界上，那么也会贡献边长
                            res += 1

        return res