"""
有一个1,000,000 x 1,000,000的矩阵，里面有一些障碍物。给你起点和终点，问你能否从起点走到终点。

这一题我第一反应还是union find，但是看到这个矩阵的尺寸就慌了，首先就没有这么大的空间来存这个图，遍历一遍所有的格子（总共有1,000,000,000,000 = 10^12个格子哟），即使每个格子只要1 ns，总共也需要1000 s，所以用union find、至少暴力union find肯定是不行的。

所以要先想办法把整个矩阵的规模减小，也就是要创造一个连接关系完全相同、但是尺寸小很多的等效矩阵。
"""

from typing import *

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if blocked == [] or source == target: # 如果一个障碍物都没有，或者一开始出发就在终点了
            return True # 那铁可以啊
        else:
            mapping = {} # 存图中节点之间的连接关系

            allNodesSortedByX = sorted(blocked + [source, target], key=lambda x: x[0]) # 把所有障碍物、连同起点、终点，按x值排序
            allNodesSortedByY = sorted(blocked + [source, target], key=lambda x: x[1]) # 按y值排序

            for i, v in enumerate(allNodesSortedByX[1: ], 1): # 压缩列
                lastNode = allNodesSortedByX[i - 1]
                if v[0] >= lastNode[0] + 3: # 如果和上一个节点之间空了2列或2列以上
                    if v == source:
                        source[0] = lastNode[0] + 2
                    if v == target:
                        target[0] = lastNode[0] + 2
                    v[0] = lastNode[0] + 2 # 就把中间的空列全部删掉

            for i, v in enumerate(allNodesSortedByY[1: ], 1): # 压缩行
                lastNode = allNodesSortedByY[i - 1]
                if v[1] >= lastNode[1] + 3: # 如果和上一个节点之间空了2行或者2行以上
                    if v == source:
                        source[1] = lastNode[1] + 2
                    if v == target:
                        target[1] = lastNode[1] + 2
                    v[1] = lastNode[1] + 2 # 把中间的空行全部删掉

            # 到这里图已经压缩好了，但是边界还需要处理一下，因为压缩完之后，如果只取能容纳所有节点的那个矩形，可能会出现矩形外面也有路径的情况
            if allNodesSortedByX[0][0] != 0: # 如果压缩完之后，出现节点的第一行不在边界上
                minRowIndex = allNodesSortedByX[0][0] - 1 # 空出一行出来，防止矩形外面正好存在路径的情况
            else: # 本来就在边界上
                minRowIndex = 0 # 那么什么都不用做

            if allNodesSortedByX[-1][0] != 10**6 - 1: # 下边界也是一样的道理
                maxRowIndex = allNodesSortedByX[-1][0] + 1
            else:
                maxRowIndex = 10**6 - 1

            if allNodesSortedByY[0][1] != 0: # 左边界
                minColumnIndex = allNodesSortedByY[0][1] - 1
            else:
                minColumnIndex = 0

            if allNodesSortedByY[-1][1] != 10** 6 - 1: # 右边界
                maxColumnIndex = allNodesSortedByY[-1][1] + 1
            else:
                maxColumnIndex = 10**6 - 1

            blocked = set(map(tuple, blocked))
            source = tuple(source)
            target = tuple(target)

            for rowIndex in range(minRowIndex, maxRowIndex + 1): # 第二次遍历，传统union find

                for columnIndex in range(minColumnIndex, maxColumnIndex + 1):
                    position = (rowIndex, columnIndex)
                    if position not in blocked:
                        mapping[position] = mapping.get(position, position)
                        neighbors = [
                            (rowIndex - 1, columnIndex),
                            # (rowIndex + 1, columnIndex),
                            (rowIndex, columnIndex - 1),
                            # (rowIndex, columnIndex + 1) # 下、右可以不用连接，因为反正之后会遍历到
                        ]

                        for neighbor in neighbors:
                            if minRowIndex <= neighbor[0] <= maxRowIndex and minColumnIndex <= neighbor[1] <= maxColumnIndex and neighbor not in blocked:
                                mapping[neighbor] = mapping.get(neighbor, neighbor)
                                self.union(mapping, position, neighbor)

            return self.isConnected(mapping, source, target)

    def union(self, mapping: dict, p: "Type", q: "Type") -> None:
        rootOfP = self.root(mapping, p)
        rootOfQ = self.root(mapping, q)
        mapping[rootOfP] = rootOfQ

    def root(self, mapping: dict, p: "Type") -> "Type":

        while p != mapping[p]:
            mapping[p] = mapping[mapping[p]]
            p = mapping[p]

        return p

    def isConnected(self, mapping: dict, p: "Type", q: "Type") -> bool:
        return self.root(mapping, p) == self.root(mapping, q)

# s = Solution()
# print(s.isEscapePossible(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2])) # false
# print(s.isEscapePossible(blocked = [[0,1],[1,0]], source = [0,0], target = [999999, 999999])) # false
# print(s.isEscapePossible(blocked = [], source = [0,0], target = [999999,999999])) # 