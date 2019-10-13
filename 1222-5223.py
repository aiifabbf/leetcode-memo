"""
给一个8x8的棋盘、皇后的位置、国王的位置，问哪些皇后可以吃掉国王。

很简单，从国王开始往8个方向（上、下、左、右、上左、上右、下左、下右）分别搜索，每个方向遇到的第一个皇后就是能吃掉国王的皇后。注意如果出现国王和皇后之间隔了另一个皇后，比如

::

    王    后1    后2

后2是没办法吃掉国王的。

但是要写的好看挺难的……我写了8个for循环。
"""

from typing import *

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set(map(tuple, queens)) # 把皇后的位置转换成tuple再放到set里，这样判断某个皇后是否存在的复杂度就是O(1)
        res = []

        for delta in range(1, 9): # 往右看
            temp = (king[0] + delta, king[1])
            if temp in queens: # 遇到的第一个皇后
                res.append(temp) # 放到结果里
                break # 然后就不用看下去了，因为反正被第一个皇后挡住了，吃不到国王了

        for delta in range(1, 9): # 往下看
            temp = (king[0], king[1] + delta)
            if temp in queens:
                res.append(temp)
                break

        for delta in range(1, 9): # 往右下看
            temp = (king[0] + delta, king[1] + delta)
            if temp in queens:
                res.append(temp)
                break

        for delta in range(1, 9): # 往左看
            temp = (king[0] - delta, king[1])
            if temp in queens:
                res.append(temp)
                break

        for delta in range(1, 9): # 往上看
            temp = (king[0], king[1] - delta)
            if temp in queens:
                res.append(temp)
                break

        for delta in range(1, 9): # 往左上看
            temp = (king[0] - delta, king[1] - delta)
            if temp in queens:
                res.append(temp)
                break

        for delta in range(1, 9): # 往右上看
            temp = (king[0] + delta, king[1] - delta)
            if temp in queens:
                res.append(temp)
                break

        for delta in range(1, 9): # 往左下看
            temp = (king[0] - delta, king[1] + delta)
            if temp in queens:
                res.append(temp)
                break

        return list(map(list, res))

# s = Solution()
# print(s.queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))
# print(s.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
# print(s.queensAttacktheKing(queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]))