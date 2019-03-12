# 很好玩的一道题。要你尽量加砖块，但是又不影响前视图和左视图。

# 挺简单的。先算出前视图、左视图。对于图上的每个元素来说，它能达到的最大高度是不影响前视图、左视图的最大高度，这个最大高度很好算，就是这个元素所在行列的前视图和左视图。比如假如这个元素在第1行第2列，那么这个元素在不影响前视图、左视图的前提下能达到的最大高度是前视图的第2个、左视图的第1个中较小的那个，即 ``min(front[2], left[1])``。

from typing import *

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        leftView = [max(i) for i in grid] # 算出左视图，很简单
        frontView = [max(grid[row][col] for row in range(len(grid))) for col in range(len(grid[0]))] # 前视图比较难算
        # print(frontView)
        # print(leftView)
        delta = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                delta += min(frontView[col], leftView[row]) - grid[row][col]

        return delta

s = Solution()
assert s.maxIncreaseKeepingSkyline([ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]) == 35