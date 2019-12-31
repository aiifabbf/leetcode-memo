"""
给几个点，测试它们在不在同一条直线上。

很简单，测试每个点和第一个点之间连线的斜率是否相等就好了。

比较麻烦的就是如果斜率不存在怎么办，用 ``inf`` 来表示就好了。
"""

from typing import *

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a = coordinates[0] # 第一个点
        b = coordinates[1] # 第二个点
        if a[0] == b[0]: # 如果斜率不存在
            slope = float("inf") # 记为inf
        else: # 如果斜率存在
            slope = (b[1] - a[1]) / (b[0] - a[0])

        for i, v in enumerate(coordinates[1: ], 1):
            if v[0] == a[0]: # 如果当前点和第一个点连线的斜率不存在
                test = float("inf")
            else:
                test = (v[1] - a[1]) / (v[0] - a[0])
            
            if test != slope: # 看当前点和第一个点连线的斜率、和第二个点和第一个点连线的斜率是否相等，如果不相等
                return False # 说明不在同一条直线上

        return True

s = Solution()
print(s.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]])) # true
print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])) # false
print(s.checkStraightLine([[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]])) # true
print(s.checkStraightLine([[-2,12],[2,-8],[6,-28],[-10,52],[-7,37],[4,-18],[7,-33],[1,-3],[-1,7],[8,-38]])) # true
print(s.checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]])) # false