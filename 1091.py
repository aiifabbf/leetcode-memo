"""
.. default-role:: math

从起点到终点的最短路径

从起点开始一圈一圈往外BFS就好了，一边遍历一边更新到每个节点的最近距离。

2019年5月面头条的时候被问过类似的题目，当时问的是每个小区到最近的快递点的距离。
"""

from typing import *

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        columnCount = len(grid[0])
        if grid[0][0] == 1:
            if rowCount == 1 and columnCount == 1:
                return 1
            else:
                return -1

        queue = [(0, 0)]
        traveled = set()
        distances = {(0, 0): 0} # distances[i] = v是从起点走到i的最小步数

        while queue:
            levelQueue = []

            for node in queue:
                neighbors = [
                    (node[0] - 1, node[1] - 1),
                    (node[0] - 1, node[1]),
                    (node[0] - 1, node[1] + 1),
                    (node[0], node[1] - 1),
                    (node[0], node[1] + 1),
                    (node[0] + 1, node[1] - 1),
                    (node[0] + 1, node[1]),
                    (node[0] + 1, node[1] + 1),
                ] # 上下左右斜向总共8个方向

                for neighbor in neighbors:
                    if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount:
                        if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in traveled and neighbor not in levelQueue:
                            distances[neighbor] = min(distances.get(neighbor, float("inf")), distances[node] + 1) # 更新距离。到neighbor的步数可能是起点到node的步数+1，但也有可能通过别的节点更近
                            levelQueue.append(neighbor)

                traveled.add(node)

            queue = levelQueue

        return distances.get((rowCount - 1, columnCount - 1), -2) + 1 # 距离 = 步数 + 1

s = Solution()
print(s.shortestPathBinaryMatrix([
    [0, 1],
    [1, 0],
])) # 2
print(s.shortestPathBinaryMatrix([
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
])) # 4
print(s.shortestPathBinaryMatrix([
    [0]
])) # 1
print(s.shortestPathBinaryMatrix([
    [1]
])) # 1