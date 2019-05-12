r"""
给两个数x, y，输出集合

.. math::

    \{x^i + y^j | i \geq 0, j \geq 0, x^i + y^j \leq B\}

"""

from typing import *

import math

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1: # 先确定i和j的范围，注意x和y可能是1的情况
            maxI = 2
        else:
            maxI = math.ceil(math.log(bound, x))
        if y == 1:
            maxJ = 2
        else:
            maxJ = math.ceil(math.log(bound, y))
        res = set()

        for i in range(0, maxI):

            for j in range(0, maxJ):
                n = x**i + y**j
                if n <= bound:
                    res.add(n)

        return list(res)

# s = Solution()
# print(s.powerfulIntegers(2, 3, 10))
# print(s.powerfulIntegers(3, 5, 15))
# print(s.powerfulIntegers(2, 1, 10))