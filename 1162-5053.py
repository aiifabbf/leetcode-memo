"""
给一个矩阵，0表示海水、1表示陆地，距离陆地最远的那块海水离陆地的距离是多少？方便起见，距离的定义采用曼哈顿距离。

用广度优先，计算出每个海水格子离最近的陆地距离是多少，然后取最大的那个值就好了。关键问题就是怎样用广度优先计算出这个距离。

粗略地讲，就是从所有陆地格子开始，一圈一圈往外扩展。所有的陆地格子距离最近的陆地的距离显然是0，陆地往外一圈的所有海水格子距离陆地格子的距离 **最大** 是1，第二圈最大是2……这样以此类推。

具体一点来说

1.  先找到所有的陆地格子，把这些陆地格子离最近的陆地的距离都设置成0，其他格子都设置成正无穷大
2.  找到所有的陆地格子周围的所有海水格子，放到一个记录待探索区域的集合里
3.  不停地迭代，遍历待探索区域集合里的海水格子，更新这些格子距离最近陆地的距离，再把这些海水格子四周的其他海水格子加入到待探索区域的集合里，直到待探索区域集合为空

怎样更新某个格子的距离呢？直接取上下左右四周的距离+1就好了，比如

::

    inf inf inf
    inf ?   1
    inf 2   inf

中间的那一个格的最近距离就是min(inf, 1, 2) + 1 = 1 + 1 = 2。

不用担心待探索区域集合空了之后，地图上还会残留有没有更新最近距离的格子，因为每次都是添加格子的上下左右四个格子，这样所有的格子都会被遍历到，不会漏掉任何一个格子。

也不用担心某个待探索的格子上下左右四周全部都是inf，比如

::

    inf inf inf
    inf ?   inf
    inf inf inf

因为更新待探索区域集合的策略是从已经探索过的格子出发，把已经探索过的格子四周的、还未探索过的格子加入到待探索区域集合里，所以这样可以保证每个格子在被探索、被更新最近距离的时候，上下左右四周至少有一个格子的最近距离是已知的、不为inf的。

隐约记得头条面试面过类似的题，好像是问用户离最近的自提柜的距离。
"""

from typing import *

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rowCount = len(grid) # 地图总共有多少行
        columnCount = len(grid[0]) # 地图总共有多少列
        nearestLandDistances = [[float("inf")] * columnCount for _ in range(rowCount)] # 地图上每一个距离最近的陆地格子的曼哈顿距离：d[i][j]表示第i行、第j列距离最近的陆地格子的曼哈顿距离
        discovered = set() # 待探索、更新距离的海水格子的坐标集合

        for rowIndex, row in enumerate(grid):
            
            for columnIndex, box in enumerate(row):
                if box == 1: # 找到所有陆地格子
                    neighbors = [
                        (rowIndex - 1, columnIndex),
                        (rowIndex + 1, columnIndex),
                        (rowIndex, columnIndex - 1),
                        (rowIndex, columnIndex + 1)
                    ] # 上下左右4个邻居

                    for neighborPosition in neighbors: # 找到陆地格子周围的所有海水格子
                        neighborRowIndex, neighborColumnIndex = neighborPosition
                        if 0 <= neighborRowIndex < rowCount and 0 <= neighborColumnIndex < columnCount: # 检查邻居在不在地图上，防止越界
                            if grid[neighborRowIndex][neighborColumnIndex] == 0: # 是海水格子
                                discovered.add(neighborPosition) # 放入待探索格子集合里

                    nearestLandDistances[rowIndex][columnIndex] = 0 # 陆地格子距离最近陆地格子的距离当然是0啦

        if not discovered: # 没有待探索的格子，说明可能地图上全都是陆地、或者全都是海水
            return -1 # 这时候根据题设直接返回-1

        while discovered: # 不停地迭代，直到没有待探索的海水格子（所有海水格子的距离都已经更新了）为止
            newlyDiscovered = set() # 这一轮迭代之后待探索的海水格子集合
            
            for position in discovered: # 更新待探索格子集合里每个海水格子的最近距离
                rowIndex, columnIndex = position
                neighbors = [
                    (rowIndex - 1, columnIndex),
                    (rowIndex + 1, columnIndex),
                    (rowIndex, columnIndex - 1),
                    (rowIndex, columnIndex + 1)
                ] # 上下左右4个邻居

                nearestLandDistance = float("inf")

                for neighborPosition in neighbors:
                    neighborRowIndex, neighborColumnIndex = neighborPosition
                    if 0 <= neighborRowIndex < rowCount and 0 <= neighborColumnIndex < columnCount: # 检查邻居在不在地图上，防止越界
                        nearestLandDistance = min(nearestLandDistance, nearestLandDistances[neighborRowIndex][neighborColumnIndex]) # 最近距离是四周邻居的最近距离+1
                        if nearestLandDistances[neighborRowIndex][neighborColumnIndex] == float("inf"): # 如果最近距离是inf，说明还没有更新，待探索
                            newlyDiscovered.add(neighborPosition) # 把还没有探索过的邻居格子加入到待探索区域集合里

                nearestLandDistances[rowIndex][columnIndex] = nearestLandDistance + 1

            discovered = newlyDiscovered
        # 出while说明地图上每个格子的最近陆地距离都更新好了，下面该寻找最远陆地距离了

        maximumDistance = -1

        for rowIndex, row in enumerate(grid): # 找到所有海水格子

            for columnIndex, box in enumerate(row):
                if box == 0: # 是海水格子
                    maximumDistance = max(maximumDistance, nearestLandDistances[rowIndex][columnIndex])

        return maximumDistance

# s = Solution()
# print(s.maxDistance([[1,0,1],[0,0,0],[1,0,1]])) # 2
# print(s.maxDistance([[1,0,0],[0,0,0],[0,0,0]])) # 4
# print(s.maxDistance([[0, 0, 0], [0, 0, 0], [0, 0, 0]])) # -1