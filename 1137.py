r"""
.. default-role:: math

定义

.. math::

    T_n = \begin{cases}
        0, & n = 0 \\
        1, & n = 1, 2 \\
        T_{n - 1} + T_{n - 2} + T_{n - 3}, & n > 2
    \end{cases}

给一个 `n` ，计算 `T_n` 的值。

递归秒做，但是注意加上cache，这样复杂度就降低到 `O(n)` 了。

有空算一下通项公式……但是感觉会很复杂。
"""

from typing import *

import functools

class Solution:
    @functools.lru_cache(None)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

# s = Solution()
# print(s.tribonacci(4)) # 4
# print(s.tribonacci(25)) # 1389537