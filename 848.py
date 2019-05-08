"""
给一个字符串S里面都是小写字母、和一个array，``array[i]`` 表示把字符串 ``S[0: i + 1]`` 里每个小写字母都循环偏移 ``array[i]`` 个单位。

循环偏移的意思是 ``z`` 偏移一个单位到 ``a`` 这种。

很简单，先把array转换成每个字母循环偏移的 **净次数** 就可以了。因为 ``array[i]`` 代表的是 ``S[0: i+1]`` 里所有偏移的单位，所以

-   ``array[-1]`` 表示最后一个字母的净偏移量
-   ``array[-2] + array[-1]`` 表示倒数第二个字母的净偏移量
-   ...
-   ``sum(array)`` 表示第一个字母的净偏移量

可见给array做一个从后往前的累加都可以得到第i个字母的净偏移量了。

得到净偏移量之后，需要解决循环的问题，也是非常简单的

1.  把当前字母的ascii减去 ``a`` 的ascii，得到当前字母ascii相对于 ``a`` 的偏移量
2.  加上净偏移量对26的余数

    也可以直接加净偏移量。

3.  再取一次对26的余数

    这样就做到了循环偏移。

4.  再加上 ``a`` 的ascii
"""

from typing import *

import itertools

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        shifts = reversed(list(itertools.accumulate(reversed(shifts)))) # 逆向累加
        res = list(S)
        ordA = ord("a")

        for i, v in enumerate(shifts):
            res[i] = chr((ord(res[i]) - ordA + v % 26) % 26 + ordA)

        return "".join(res)

# s = Solution()
# print(s.shiftingLetters("abc", [3, 5, 9])) # rpl