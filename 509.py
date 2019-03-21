"""
老生常谈的斐波那契数列……

最好的当然是直接用通项公式，复杂度 :math:`O(1)` ，但是有可能会因为浮点数运算精度的问题还要四舍五入。

稍微慢一点的就是加cache再递归，复杂度 :math:`O(n)` 吧（姑且把那个n次方看成常数时间吧）。
"""

from typing import *

import functools

class Solution:
    @functools.lru_cache(None)
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)