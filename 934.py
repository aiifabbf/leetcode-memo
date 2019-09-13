"""
图上有两个岛，问需要造多长的一个桥能把两个岛连起来，桥的长度要尽量短。

这道题里面，我用了union find和图的广度优先搜索

1.  先用union find把连在一起的陆地都挑出来，识别出第一个岛和第二个岛
2.  然后从第一个岛开始，一圈一圈往外，用图的广度优先搜索，更新图上每一块区域（包括属于第二个岛的陆地）到第一个岛的最近距离
3.  遍历第二个岛上的每块区域，得到第二个岛离第一个岛的最近距离，减去1，就是需要造桥的长度了
"""

from typing import *

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        mapping = dict() # 给union find用来记录点之间的连通关系
        rowCount = len(A) # 图有多少行
        columnCount = len(A[0]) # 图有多少列

        for rowIndex, row in enumerate(A): # 遍历一遍图上的每块区域，目的是要摸清陆地之间的连通关系，以便后续识别出两个岛

            for columnIndex, box in enumerate(row):
                if box == 1:
                    position = (rowIndex, columnIndex)
                    land1 = position # 就假设最后一次遍历到的陆地是第一个岛了
                    mapping[position] = mapping.get(position, position)
                    neighbors = [
                        (rowIndex - 1, columnIndex),
                        (rowIndex + 1, columnIndex),
                        (rowIndex, columnIndex - 1),
                        (rowIndex, columnIndex + 1)
                    ] # 上下左右四个相邻的区域

                    for neighbor in neighbors: # 遍历这块区域周围四个相邻的区域
                        if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount: # 防止越界
                            if A[neighbor[0]][neighbor[1]] == 1: # 如果是陆地的话
                                mapping[neighbor] = mapping.get(neighbor, neighbor)
                                self.union(mapping, (rowIndex, columnIndex), neighbor) # 连起来

        # 这里出来之后，两个岛上的陆地形成了两个不相连的图，下面要把第二个岛上的某块陆地挑出来

        # -----以上是union find的部分-----

        for position in mapping.keys(): # 遍历图上的每块陆地
            if not self.isConnected(mapping, land1, position): # 一旦发现某一块陆地和第一个岛不相连
                land2 = position # 那么这块陆地肯定是属于第二个岛的了
                break

        # 出来之后，land1就表示第一个岛上的某块陆地，land2表示第二个岛上的某块陆地

        # -----以下是图的BFS的部分-----

        discovered = set() # 已经探索过的、但还未更新距离的区域的坐标
        nearestDistanceToLand1 = [[float("inf")] * columnCount for _ in range(rowCount)] # nearestDistanceToLand1[i][j]表示(i, j)距离第一个岛的最近距离

        for position in mapping.keys(): # 遍历第一个岛上的每块陆地，把第一个岛周围的海水区域选出来，放到discovered集合里
            if self.isConnected(mapping, land1, position): # 一定要是第一个岛上的陆地才行
                rowIndex, columnIndex = position
                nearestDistanceToLand1[rowIndex][columnIndex] = 0 # 第一个岛上任意一块陆地距离第一个岛的距离当然是0啦
                neighbors = [
                    (rowIndex - 1, columnIndex),
                    (rowIndex + 1, columnIndex),
                    (rowIndex, columnIndex - 1),
                    (rowIndex, columnIndex + 1)
                ] # 这块陆地上下左右四周的区域

                for neighbor in neighbors: # 遍历这块陆地周围的区域
                    if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount: # 防止越界
                        if A[neighbor[0]][neighbor[1]] == 0: # 如果是海水的话
                            discovered.add(neighbor) # 加入到discovered集合里，待更新距离

        while discovered: # 接下来开始就是图的广度优先搜索了。不断迭代，直到知道图上每一个区域离第一个岛的最近距离为止
            newlyDiscovered = set() # 这一轮里发现的新的待更新距离的区域

            for position in discovered: # 遍历每个待更新距离的区域，更新它们到第一个岛的距离
                rowIndex, columnIndex = position
                neighbors = [
                    (rowIndex - 1, columnIndex),
                    (rowIndex + 1, columnIndex),
                    (rowIndex, columnIndex - 1),
                    (rowIndex, columnIndex + 1)
                ]

                neighborNearestDistanceToLand1 = float("inf") # 这个区域四周的其他区域距离第一个岛的最近距离

                for neighbor in neighbors: # 遍历这个区域四周的区域
                    if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount: # 防止越界
                        neighborNearestDistanceToLand1 = min(neighborNearestDistanceToLand1, nearestDistanceToLand1[neighbor[0]][neighbor[1]]) # 取周围四个区域到第一个岛的最近距离的最小值
                        if nearestDistanceToLand1[neighbor[0]][neighbor[1]] == float("inf"): # 如果发现周围的区域到第一个岛的距离还未更新
                            newlyDiscovered.add(neighbor) # 就加入到待更新集合里，等下一轮迭代来更新

                nearestDistanceToLand1[rowIndex][columnIndex] = neighborNearestDistanceToLand1 + 1 # 因为四周区域到这个区域的距离是1，所以当前区域到第一个岛的最近距离，就是当前区域四周的其他区域到第一个岛的最近距离的最小值再加上1

            discovered = newlyDiscovered

        # 这里出来之后，nearestDistanceToLand1上就没有inf了，我们知道了图上每一块区域到第一个岛的最近距离了。下面就要遍历第二个岛的每一块陆地，找到第二个岛上离第一个岛最近的陆地是哪一块、这块陆地离第一个岛的距离是多少

        res = float("inf") # 记录第二个岛到第一个岛的最近距离

        for position in mapping.keys():
            if self.isConnected(mapping, position, land2): # 和land2相连说明这块陆地是属于第二个岛的
                res = min(res, nearestDistanceToLand1[position[0]][position[1]]) # 更新一下

        # 出来之后，res存的数字就是第二个岛到第一个岛的最近距离啦，这个最近距离再减去1，就是最短的桥的长度啦

        return res - 1

    # 俗套的union find
    def union(self, mapping: dict, p: "Type", q: "Type"):
        rootOfP = self.root(mapping, p)
        rootOfQ = self.root(mapping, q)
        mapping[rootOfP] = rootOfQ

    def root(self, mapping: dict, r: "Type") -> "Type":

        while r != mapping[r]:
            mapping[r] = mapping[mapping[r]]
            r = mapping[r]

        return r

    def isConnected(self, mapping: dict, p: "Type", q: "Type") -> bool:
        rootOfP = self.root(mapping, p)
        rootOfQ = self.root(mapping, q)
        return rootOfP == rootOfQ


s = Solution()
print(s.shortestBridge([
    [0, 1],
    [1, 0],
])) # 1
print(s.shortestBridge([
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 1],
])) # 2
print(s.shortestBridge([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
])) # 1