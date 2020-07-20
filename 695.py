"""
.. default-role:: math

最大的岛屿的面积

给一个二维矩阵， ``1`` 表示陆地， ``0`` 表示海水。上下左右紧密相连的才视为相连。找到最大的岛屿的面积。

很简单，用union find扫一遍，统计每个岛屿的面积，返回那个最大的面积就好了。
"""

from typing import *


class UnionFindGraph(dict):
    def isConnected(self, p: Hashable, q: Hashable) -> bool:
        return self.root(p) == self.root(q)

    def root(self, p: Hashable) -> Hashable:

        while p != self[p]:
            self[p] = self[self[p]]
            p = self[p]

        return p

    def union(self, p: Hashable, q: Hashable):
        rootOfP = self.root(p)
        rootOfQ = self.root(q)

        self[rootOfP] = rootOfQ

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        columnCount = len(grid[0])

        graph = UnionFindGraph() # 用union find先扫一遍

        for rowIndex, row in enumerate(grid):

            for columnIndex, box in enumerate(row):
                if box == 1:
                    position = (rowIndex, columnIndex)
                    graph[position] = graph.get(position, position)
                    neighbors = [
                        (rowIndex - 1, columnIndex),
                        (rowIndex + 1, columnIndex),
                        (rowIndex, columnIndex - 1),
                        (rowIndex, columnIndex + 1),
                    ]

                    for neighbor in neighbors:
                        if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount:
                            if grid[neighbor[0]][neighbor[1]] == 1:
                                graph[neighbor] = graph.get(neighbor, neighbor)
                                graph.union(position, neighbor)

        rootClusterMapping = dict() # rootClusterMapping[graph.root(position)]是position处的陆地所在的岛屿里所有地面的位置

        for v in graph.keys():
            root = graph.root(v)
            if root in rootClusterMapping:
                rootClusterMapping[root].add(v)
            else:
                rootClusterMapping[root] = {v}

        return max((len(v) for k, v in rootClusterMapping.items()), default=0)