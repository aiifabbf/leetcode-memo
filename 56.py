# 找到区间列里面互相有重合的区间并且把它们合并起来。

from typing import *

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if intervals == []:
            return []

        intervals = sorted(intervals, key=lambda interval: interval.start)
        q = []
        while True:
            if len(intervals) == 1:
                return q + intervals

            a = intervals.pop(0)
            b = intervals.pop(0)
            if a.end >= b.start:
                c = Interval(a.start, max(a.end, b.end))
                intervals.insert(0, c)
            else:
                q.append(a)
                intervals.insert(0, b)
