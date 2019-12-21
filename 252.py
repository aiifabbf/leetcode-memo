"""
给一些左闭右开区间代表时间，它们是否两两兼容？

很简单，先按起始时间排序，然后两个两个（两个两个的意思是，先看12、再看23、再看34这样，不是先看12、再看34、再看56）看是否兼容。
"""

from typing import *

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if intervals == []: # 记得处理空的时候
            return True

        intervals.sort(key=lambda v: v[0]) # 按起始时间排序
        lastInterval = intervals[0] # 上一个区间

        for v in intervals[1: ]:
            if lastInterval[1] > v[0]: # 两个两个比较是否兼容
                return False
            else:
                lastInterval = v

        return True

# s = Solution()
# print(s.canAttendMeetings([[0,30],[5,10],[15,20]]))
# print(s.canAttendMeetings([[7,10],[2,4]]))