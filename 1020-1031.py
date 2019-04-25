"""
存在路径能走到地图边界的格子的个数。地图以一个二维矩阵的形式给你，0表示海、1表示陆地。

我的第一反应就是union find，遍历这个矩阵的每一个格子，把相邻的陆地连接起来；边界可以看成是一个特殊的节点，矩阵上下左右边界上的陆地都和“边界”这个节点连接起来。然后再遍历一边，判断每个陆地格子是否和“边界”这个节点之间存在路径。

Union find是Princeton Algorithms课的第一节内容，所以最近看过，印象很深刻。

快速判断一个节点和另一个节点之间是否存在路径的关键是，把所有有路径相连的节点都放在同一个树里，并且这个树的深度越小越好，这样判断是否存在路径的时候，只要判断两个节点所在树的根节点是否是同一个节点就可以了。
"""

from typing import *

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if A == []:
            return 0

        boundary = (float("inf"), float("inf")) # 上下左右边界用一个特殊的“边界”节点来表示就可以了
        mapping = {
            boundary: boundary
        } # 这个dict用来存节点之间的连接关系，(key, value)表示key的父节点是value

        for rowIndex, row in enumerate(A):

            for columnIndex, box in enumerate(row):
                if box == 1:
                    position = (rowIndex, columnIndex)
                    mapping[position] = mapping.get(position, position)
                    if rowIndex == 0: # 第一行。这一行的所有陆地都和上边界接壤
                        self.union(mapping, position, boundary)
                    if rowIndex == len(A) - 1: # 最后一行。这一行的所有陆地都和下边界接壤
                        self.union(mapping, position, boundary)
                    if columnIndex == 0: # 第一列。这一列的所有陆地都和左边界接壤
                        self.union(mapping, position, boundary)
                    if columnIndex == len(A[0]) - 1: # 最后一列。这一列的所有陆地都和右边界接壤
                        self.union(mapping, position, boundary)
                    
                    if rowIndex - 1 >= 0: # 看一下正上方是不是陆地
                        if A[rowIndex - 1][columnIndex] == 1: # 如果是陆地
                            self.union(mapping, position, (rowIndex - 1, columnIndex)) # 就连接起来
                    if columnIndex - 1 >= 0: # 看一下正左方是不是陆地
                        if A[rowIndex][columnIndex - 1] == 1: # 如果是陆地
                            self.union(mapping, position, (rowIndex, columnIndex - 1)) # 就连接起来

                    # 右、下方可以暂时不用管，因为反正后面会遍历到
                    # if rowIndex + 1 <= len(A) - 1:
                    #     if A[rowIndex + 1][columnIndex] == 1:
                    #         self.union(mapping, position, (rowIndex + 1, columnIndex))
                    # if columnIndex + 1 <= len(A[0]) - 1:
                    #     if A[rowIndex][columnIndex + 1] == 1:
                    #         self.union(mapping, position, (rowIndex, columnIndex + 1))

        res = 0

        for rowIndex, row in enumerate(A):

            for columnIndex, box in enumerate(row):
                if box == 1:
                    position = (rowIndex, columnIndex)
                    if not self.isConnected(mapping, position, boundary): # 如果当前的这个陆地没有连接到边界
                        res = res + 1 # 发现了一个满足条件的陆地

        return res

    def union(self, mapping: dict, p: Type, q: Type) -> None: # 建立连接关系
        rootOfP = self.root(mapping, p) # 找到p所在树的根节点
        rootOfQ = self.root(mapping, q) # 找到q所在树的根节点
        mapping[rootOfP] = rootOfQ # 把p所在的树的根节点贴到q所在的树的根节点上

    def isConnected(self, mapping: dict, p: Type, q: Type) -> bool: # 判断两个节点之间是否存在路径相连
        return self.root(mapping, p) == self.root(mapping, q) # 只要判断两个节点是否在同一个树里就可以了，等效为判断两个节点所在树的根节点是否是同一个节点

    def root(self, mapping: dict, r: Type) -> Type: # 得到某个节点所在树的根节点

        while r != mapping[r]: # 如果当前节点的父节点不是自身，说明当前节点不是根节点
            mapping[r] = mapping[mapping[r]] # 这一句话是避免树过深的关键
            r = mapping[r]

        return r

# s = Solution()
# print(s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])) # 3
# print(s.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])) # 0
# print(s.numEnclaves([[0, 1, 1, 1]])) # 0
# print(s.numEnclaves([
#     [0,0,0,1,1,1,0,1,0,0],
#     [1,1,0,0,0,1,0,1,1,1],
#     [0,0,0,1,1,1,0,1,0,0],
#     [0,1,1,0,0,0,1,0,1,0],
#     [0,1,1,1,1,1,0,0,1,0],
#     [0,0,1,0,1,1,1,1,0,1],
#     [0,1,1,0,0,0,1,1,1,1],
#     [0,0,1,0,0,1,0,1,0,1],
#     [1,0,1,0,1,1,0,0,0,0],
#     [0,0,0,0,1,1,0,0,0,1]]
# )) # 3