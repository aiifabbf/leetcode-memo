"""
给一个1-9之间的整数n，问你从1到n的各种排列里，第k个是哪个。

比如给 :math:`n = 3, k = 3` ，先给出 ``1, 2, 3`` 的所有排列方式

::

    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1

算了，先用万能的 ``itertools.permutations()`` 过吧……
"""

from typing import *

import itertools

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        for i, v in enumerate(itertools.permutations(range(1, n + 1))):
            if i == k - 1:
                return "".join(map(str, v))

# s = Solution()
# print(s.getPermutation(3, 3))