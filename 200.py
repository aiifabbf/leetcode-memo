"""
地图上有几座孤立岛屿？地图是二维的，1表示陆地，0表示水。岛屿的定义是，这个岛屿里所有的方块上下左右都不和其他岛屿相邻。

典型的union find，一座岛屿上的所有方块最后都会出现同一棵树里，所以最后只要数有多少棵树，即数有多少个根节点，就可以了。
"""

from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        mapping = {}

        for rowIndex, row in enumerate(grid):

            for columnIndex, box in enumerate(row):
                position = (rowIndex, columnIndex)
                if box == "1":
                    mapping[position] = mapping.get(position, position) # 这里有个坑，当前格子可能上次（比如正好是上一行的某个格子的正下方的相邻格子）已经被union过了，所以mapping中已经有记录了
                    neighbors = [
                        (rowIndex - 1, columnIndex), # 上方
                        (rowIndex + 1, columnIndex), # 下方
                        (rowIndex, columnIndex - 1), # 左边
                        (rowIndex, columnIndex + 1), # 右边
                    ]

                    for neighbor in neighbors:
                        try: # 用try，省得再判断越界了
                            if grid[neighbor[0]][neighbor[1]] == "1": # 如果相邻的各自是陆地的话
                                mapping[neighbor] = mapping.get(neighbor, neighbor)
                                self.union(mapping, position, neighbor) # 连起来
                        except:
                            pass

        rootSet = set(self.root(mapping, p) for p in mapping)
        return len(rootSet)

    def union(self, mapping: dict, p: Type, q: Type) -> None:
        rootOfP = self.root(mapping, p)
        rootOfQ = self.root(mapping, q)
        mapping[rootOfP] = rootOfQ

    def root(self, mapping: dict, p: Type) -> Type:

        while p != mapping[p]:
            mapping[p] = mapping[mapping[p]]
            p = mapping[p]

        return p

    def isConnected(self, mapping: dict, p: Type, q: Type) -> bool:
        return self.root(mapping, p) == self.root(mapping, q)

# s = Solution()
# print(s.numIslands([
#     "11110",
#     "11010",
#     "11000",
#     "00000"
# ])) # 1
# print(s.numIslands([
#     "11000",
#     "11000",
#     "00100",
#     "00011"
# ])) # 3