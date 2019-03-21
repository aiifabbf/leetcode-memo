"""
模拟竖式运算。

我的做法是不管其他的，首先先把K也变成 ``List[int]`` ，然后在左端补零，让两个数字位数一样。然后就按竖式运算规则来，每次除了要把两个位上的数加起来，还要加上一位进过来的进位carry，记得先把进位标志清零，然后判断这个加出来的数有没有进位（大于等于10），再置进位标志。最后算出每一位的结果之后，最后看看有没有进位，如果有的话，最左边最高位再加个1。

发现了py的几个坑

-   ``list`` 的 ``.append()`` 似乎是比 ``.insert()`` 要快的
-   ``list`` 取一下倒序 ``list[:: -1]`` 是非常非常慢的
"""

from typing import *

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # return [int(q) for q in str(sum(v * 10 ** i for i, v in enumerate(A[:: -1])) + K)] # 直接暴力转换成int再加再转回来会超时
        K = [int(i) for i in str(K)]
        maximumDigitLength = max(len(A), len(K))
        K = [0] * (maximumDigitLength - len(K)) + K
        A = [0] * (maximumDigitLength - len(A)) + A
        carry = 0
        res = []

        for i in range(len(K)):
            # digit = K[:: -1][i] + A[:: -1][i] + carry # list[:: -1]这个操作超级慢的……580 ms -> 68 ms
            digit = K[maximumDigitLength -  i - 1] + A[maximumDigitLength - i - 1] + carry
            carry = 0
            if digit >= 10:
                carry = 1
                digit -= 10
            res.append(digit) # 一个缩进错误引发的悲剧……
            # 虽然接下来返回结果的时候还要倒一次res，但是如果这里每次都是.insert()的话也是很慢的……说明append比insert要快。

        if carry == 1:
            return [1] + res[:: -1]
        else:
            return res[:: -1]