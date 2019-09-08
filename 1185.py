"""
给一个日期，返回这一天是星期几。

没什么好说的，调包侠就好了。
"""

from typing import *

import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = datetime.date(year, month, day)
        return ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")[date.weekday()] # date.weekday() == 0表示星期一

# s = Solution()
# print(s.dayOfTheWeek(31, 8, 2019)) # Saturday
# print(s.dayOfTheWeek(18, 7, 1999)) # Sunday
# print(s.dayOfTheWeek(15, 8, 1993)) # Sunday