r"""
.. default-role:: math

给一个 `m \times n` 的矩阵 ``mat`` 和一个整数 `K` ，返回一个新的矩阵 ``answer`` 使得 ``answer[i][j]`` 是子矩阵 ``mat[i - K: i + K + 1, j - K: j + K + 1]`` 的和。

又是二维前缀和。老生常谈了。设 ``integral[i][j]`` 是子矩阵 ``mat[0: i, 0: j]`` 的和，它这边 ``answer[i][j]`` 也是算一个子矩阵的和，只是要注意一下越界检查而已。
"""

from typing import *

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        rowCount = len(mat)
        columnCount = len(mat[0])
        integral = [[0] * (columnCount + 1) for _ in range(rowCount + 1)]

        for rowIndex in range(1, rowCount + 1):

            for columnIndex in range(1, columnCount + 1):
                integral[rowIndex][columnIndex] = mat[rowIndex - 1][columnIndex - 1] + integral[rowIndex - 1][columnIndex] + integral[rowIndex][columnIndex - 1] - integral[rowIndex - 1][columnIndex - 1]

        res = [[0] * columnCount for _ in range(rowCount)]

        for rowIndex, row in enumerate(mat):

            for columnIndex, value in enumerate(row):

                a = max(rowIndex - K, 0)
                b = min(rowIndex + K + 1, rowCount) # 左上角坐标是(a, b)，注意不要越界。超出的部分算0
                x = max(columnIndex - K, 0)
                y = min(columnIndex + K + 1, columnCount) # 右下角坐标是(x, y)，同样要注意不要越界

                res[rowIndex][columnIndex] = integral[b][y] + integral[a][x] - integral[a][y] - integral[b][x] # 计算子矩阵和

        return res

s = Solution()
print(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1)) # [[12,21,16],[27,45,33],[24,39,28]]
print(s.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2)) # [[45,45,45],[45,45,45],[45,45,45]]