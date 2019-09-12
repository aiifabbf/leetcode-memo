"""
实现图片模糊效果。

很简单，按题目意思来，取当前像素和周围一圈8个像素做个平均就好了，如果周围一圈没有8个像素（比如边界处的像素）就把周围有的像素放进来做个平均。
"""

from typing import *

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rowCount = len(M)
        columnCount = len(M[0])
        res = [[0] * columnCount for _ in range(rowCount)] # 模糊后的图片

        for rowIndex, row in enumerate(M): # 遍历每个像素
            
            for columnIndex, box in enumerate(row):
                neighbors = [ # 周围8个像素
                    (rowIndex - 1, columnIndex - 1),
                    (rowIndex - 1, columnIndex),
                    (rowIndex - 1, columnIndex + 1),
                    (rowIndex, columnIndex - 1),
                    (rowIndex, columnIndex + 1),
                    (rowIndex + 1, columnIndex - 1),
                    (rowIndex + 1, columnIndex),
                    (rowIndex + 1, columnIndex + 1)
                ]
                summation = box
                count = 0 # 周围有多少个像素

                for neighbor in neighbors:
                    if 0 <= neighbor[0] < rowCount and 0 <= neighbor[1] < columnCount: # 要保证周围的像素存在
                        summation = summation + M[neighbor[0]][neighbor[1]]
                        count = count + 1

                res[rowIndex][columnIndex] = summation // (count + 1) # 做平均

        return res

# s = Solution()
# print(s.imageSmoother([
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]))
# print(s.imageSmoother([
#     [2,3,4],
#     [5,6,7],
#     [8,9,10],
#     [11,12,13],
#     [14,15,16]
# ]))