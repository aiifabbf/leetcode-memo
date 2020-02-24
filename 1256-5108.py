"""
把数字按照某个规律编码。

这个规律是这样的

::

    0   ""
    1   "0"
    2   "1"
    3   "00"
    4   "01"
    5   "10"
    6   "11"
    7   "000"

我猜之后大概是

::

    8   "001"
    9   "010"
    10  "011"
    11  "100"
    12  "101"
    13  "110"
    14  "111"
    15  "0000"

感觉像是某种奇怪的二进制。为了看出规律不如把这些数字原来的二进制表示放在旁边

::

    0   0   ""
    1   1   "0"
    2   10  "1"
    3   11  "00"
    4   100 "01"
    5   101 "10"
    6   110 "11"

差不多了……规律已经找到了。如果你一行一行看大概很难找到规律，但是如果你斜着看，你会发现2的 ``10`` 去掉最前面的 ``1`` 就是1的编码 ``0`` 、6的 ``110`` 去掉最前面的 ``1`` 就是5的编码 ``10``。

所以代码就一行。
"""

from typing import *

class Solution:
    def encode(self, num: int) -> str:
        # if num == 0:
        #     return ""
        # else:
        #     num = num
        #     n = -1

        #     while 2 ** n - 1 <= num:
        #         n += 1

        #     n -= 1
        #     length = int(2 ** n).bit_length()
        #     return "{:0>30}".format(bin(num - 2 ** n + 1)[2: ])[- length + 1: ]

        return bin(num)[3: ] # 居然是这么简单的规律，输了输了

s = Solution()
print(s.encode(0)) # ""
print(s.encode(23)) # "1000"
print(s.encode(107)) # "101100"
print(s.encode(3)) # "00"