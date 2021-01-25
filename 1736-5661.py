"""
.. default-role:: math

给个24小时制的pattern，类似 ``2?:?0`` ， ``?`` 能匹配任何数字，但是要保证小时和分钟的范围正确，比如不能出现 ``25`` 小时、 ``70`` 分钟。问匹配成功的最大时间是多少？

比如和 ``2?:?0`` 能匹配成功的最大时间是 ``23:50`` 。

Rust版本里我写的方法是暴力测试每个时间，从23:59往下测试到00:00，直到出现一个匹配成功的时间。虽然有点暴力，不过最差情况也只要测试24 * 60个时间，不是很多，写起来也非常方便。

这里的Python版本写的是从pattern入手，处理每一种pattern，例如对于第一段小时来说，总共有四种可能的pattern

-   第一位和第二位都是问号

    那么最大的数字是23

-   第一位是问号、第二位是数字

    需要分情况

    -   如果第二位的数字大于等于4，那么第一位最大只能是1，否则会出现24、29这样的情况。
    -   如果第二位的数字小于4，那么第一位最大可以是2，比如23，22。

-   第一位是数字、第二位是问号

    也需要分情况

    -   如果第一位的数字是2，那么第二位最大只能是3，否则会出现24、29这样的情况。
    -   如果第一位的数字小于2，那么第二位最大可以是9。比如09、19。

-   第一位和第二位都是数字

    没办法了，只能是这个数字了。

对于第二段的分钟来说也是差不多的处理方法。

挺啰嗦的，不过应该比暴力搜索快很多。
"""

from typing import *


class Solution:
    def maximumTime(self, time: str) -> str:
        hour, minute = time.split(":")
        # 或者也可以这样处理每种pattern，我觉得挺丑的
        if hour[0] == "?" and hour[1] == "?": # 都是问号
            hour = "23"
        elif hour[0] == "?" and hour[1] != "?": # 第一位是问号、第二位是数字
            if int(hour[1]) < 4:
                hour = "2" + hour[1]
            else:
                hour = "1" + hour[1]
        elif hour[0] != "?" and hour[1] == "?": # 第一位是数字、第二位是问号
            if int(hour[0]) == 2:
                hour = hour[0] + "3"
            else:
                hour = hour[0] + "9"
        # 第一位、第二位都是数字的情况

        if minute[0] == "?" and minute[1] == "?":
            minute = "59"
        elif minute[0] == "?" and minute[1] != "?":
            minute = "5" + minute[1]
        elif minute[0] != "?" and minute[1] == "?":
            minute = minute[0] + "9"

        return ":".join([hour, minute])


s = Solution()
print(s.maximumTime("2?:?0"))
print(s.maximumTime("0?:3?"))
print(s.maximumTime("1?:22"))