"""
给一个array，里面每个元素都是24小时制的时间，问其中最短的时间间隔是多少分钟。

挺简单的，先全部转换成分钟，再排序，再复制一遍，因为可能出现循环，比如 ``23:59`` 和 ``0:00`` 其实只差1分钟，但是如果不复制，会认为相差了23 * 60 + 59分钟。
"""

from typing import *

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minuteStamps = sorted(int(time.split(":")[0]) * 60 + int(time.split(":")[1]) for time in timePoints) # 全部转换成分钟表示的时间，并且排序
        minuteStamps = minuteStamps + [time + 1440 for time in minuteStamps] # 复制一遍
        minimumDelta = 1440 # 记录最小时间间隔

        for i, v in enumerate(minuteStamps[1: ], 1):
            minimumDelta = min(minimumDelta, v - minuteStamps[i - 1])

        return minimumDelta

# s = Solution()
# print(s.findMinDifference(["23:59","00:00"])) # 1
# print(s.findMinDifference(["00:00","23:59","00:00"]
# )) # 0