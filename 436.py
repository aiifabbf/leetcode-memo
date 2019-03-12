# 感觉大致意思是，对于区间列里面的每一个区间 :math:`(i, j)` 都要从区间列里面找到另一个区间 :math:`(k, l)` 使得 :math:`k \geq j`，并且k越小越好。

from typing import *

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def findRightInterval(self, intervals: List[Interval]) -> List[int]:
        if len(intervals) <= 1:
            return [-1]

        startPositionMap = {}
        for index, value in enumerate(intervals):
            startPositionMap[value.start] = index

        maxStart = max(intervals, key=lambda x: x.start).start
        minStart = min(intervals, key=lambda x: x.start).start

        