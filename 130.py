"""
把矩阵里所有不和边界连通的 ``O`` 变成 ``X``

用BFS和union find都可以做，复杂度阶数一样，但是BFS只要遍历一遍、union find要遍历两遍，所以BFS稍微快一点。

我这里用union find做的，边界用一个虚节点表示，然后遍历矩阵中的每一个点，把边界上的 ``O`` 和虚节点连通起来，中间的 ``O`` 和上下左右相邻的 ``O`` 连通起来，遍历完成之后，就能够知道矩阵中所有 ``O`` 形成了哪几个聚类、哪个聚类是和边界虚节点连通的。

第二遍遍历的时候，只要看这个节点 ``O`` 是否和虚节点连通就可以了，如果不连通，就把它变成 ``X`` 。

.. 这个虚节点其实也不虚，可以看做是复平面上的无穷远点嘻嘻。
"""

from typing import *

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        boundary = (float("inf"), float("inf")) # 表示边界的虚节点
        mapping = {
            boundary: boundary
        } # 用来存聚类、连通关系

        for rowIndex, row in enumerate(board): # 第一次遍历，目的是生成连通关系图

            for columnIndex, box in enumerate(row):
                position = (rowIndex, columnIndex)
                if box == "O":
                    mapping[position] = mapping.get(position, position)
                    if rowIndex == 0 or rowIndex == len(board) - 1 or columnIndex == 0 or columnIndex == len(row) - 1: # 如果这个O在上下左右边界上
                        self.union(mapping, position, boundary) # 把它和边界虚节点连通起来
                    neighbors = [
                        (rowIndex - 1, columnIndex),
                        (rowIndex + 1, columnIndex),
                        (rowIndex, columnIndex - 1),
                        (rowIndex, columnIndex + 1)
                    ]

                    for neighbor in neighbors: # 看上下左右有没有相邻的O节点
                        if 0 <= neighbor[0] < len(board) and 0 <= neighbor[1] < len(row) and board[neighbor[0]][neighbor[1]] == "O":
                            mapping[neighbor] = mapping.get(neighbor, neighbor) # 有就连通起来
                            self.union(mapping, position, neighbor)

        for rowIndex, row in enumerate(board): # 第二次遍历，才是真正修改数据

            for columnIndex, box in enumerate(row):
                position = (rowIndex, columnIndex)
                if box == "O" and not self.isConnected(mapping, position, boundary): # 如果和边界没有连通起来
                    board[rowIndex][columnIndex] = "X" # 变成X

    # 下面是老生常谈的union find模板
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