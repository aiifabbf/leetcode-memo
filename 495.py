# 看到这个题我怎么感觉有点像求卷积……

from typing import *

# 卷积做法
# import numpy as np
# class Solution:
#     def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#         f = np.zeros((timeSeries[-1] - timeSeries[0] + 2, ))
#         f[timeSeries] = 1
#         g = np.ones((duration, ))
#         return np.sum(np.convolve(f, g) != 0)

# 还是不用卷积了吧……

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        totalTime = duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] >= duration: # 没有重叠
                totalTime += duration
            elif timeSeries[i] == timeSeries[i - 1]: # 完全重叠
                continue
            else: # 部分重叠
                totalTime += duration - (duration - timeSeries[i] + timeSeries[i - 1]) # 去掉重叠部分

        return totalTime

s = Solution()
print(s.findPoisonedDuration([1, 4], 2))
print(s.findPoisonedDuration([1, 2], 2))

print(s.findPoisonedDuration([1, 1], 2))
print(s.findPoisonedDuration([1, 2, 3, 4, 5], 5))