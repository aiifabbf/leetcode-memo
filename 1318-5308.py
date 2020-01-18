"""
.. default-role:: math

给三个正整数 `a, b, c` 。最少需要翻转 `a, b` 中多少个bit，才能使得 `a` 按位或 `b` 的结果是 `c` ？

先得到 `a, b, c` 的二进制表示，然后在高位补零、对齐成同样位数的二进制数，再一位一位分情况讨论就好啦。

-   如果 `c` 的第 `k` 位是0

    根据真值表

    -   ``0 & 0 == 0``
    -   ``1 & 0 == 1``
    -   ``0 & 1 == 1``
    -   ``1 & 1 == 1``

    只有 `a, b` 的第 `k` 位都是0的时候，才满足要求。所以

    -   ``a[k] == 0, b[k] == 0`` ，不用翻转
    -   ``a[k] == 1, b[k] == 0`` ，翻转1次
    -   ``a[k] == 0, b[k] == 1`` ，翻转1次
    -   ``a[k] == 1, b[k] == 1`` ，翻转2次

-   如果 `c` 的第 `k` 位是0

    还是根据真值表，只需要 `a, b` 的第 `k` 位有1个1就行了，当然2个1也没问题。但是如果没有1的话，就需要翻转一下

    -   ``a[k] == 0, b[k] == 0`` ，翻转1次
    -   ``a[k] == 1, b[k] == 0`` ，不用翻转
    -   ``a[k] == 0, b[k] == 1`` ，不用翻转
    -   ``a[k] == 1, b[k] == 1`` ，不用翻转
"""

from typing import *

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2: ][:: -1]
        b = bin(b)[2: ][:: -1]
        c = bin(c)[2: ][:: -1] # 分别得到a, b, c的二进制表示，然后颠倒过来，把低位写在最前面、高位写在后面
        length = max(map(len, (a, b, c))) # 看看a, b, c中哪个长度最大
        a = a + "0" * max(length - len(a), 0)
        b = b + "0" * max(length - len(b), 0)
        c = c + "0" * max(length - len(c), 0) # 对齐a, b, c，在高位补0
        res = 0 # 翻转次数

        for i, v in enumerate(c): # 遍历c的二进制表示的每一位
            if v == "0": # 如果这一位是0
                if a[i] == "1" and b[i] == "1": # a[k], b[k]全是1的时候需要翻转2次
                    res += 2
                elif a[i] == "0" and b[i] == "1": # a[k], b[k]有某个是1的时候，要翻转成0
                    res += 1
                elif a[i] == "1" and b[i] == "0": # 同理
                    res += 1
                else: # a[k], b[k]都是0
                    continue # 不用翻转
            else: # v == "1"
                if a[i] == "0" and b[i] == "0": # 只有a[k], b[k]全是0的时候，才要翻转1次
                    res += 1
                else: # 其他情况
                    continue # 都不用翻转

        return res

s = Solution()
print(s.minFlips(2, 6, 5)) # 3
print(s.minFlips(4, 2, 7)) # 1
print(s.minFlips(1, 2, 3)) # 0
print(s.minFlips(8, 3, 5)) # 3