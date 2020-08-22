"""
.. default-role:: math

给十进制数加千分位分隔符

比如把 ``123456789`` 变成 ``123.456.789`` 。

先把数字颠倒一下，把最低位放在最左边、最高位放在最右边，然后遇到是3的倍数的地方就插一个点。完事之后再颠倒回来。
"""

from typing import *


class Solution:
    def thousandSeparator(self, n: int) -> str:
        string = str(n)[:: -1]
        res = []

        for i in range(len(string)):
            if i % 3 == 0 and i != 0:
                res.append(".")
            res.append(string[i])

        return "".join(res)[:: -1]


s = Solution()
print(s.thousandSeparator(987))
print(s.thousandSeparator(1234))
print(s.thousandSeparator(123456789))
print(s.thousandSeparator(0))
