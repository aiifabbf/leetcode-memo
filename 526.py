"""
问满足一种特定性质的1到N的排列一共有多少种。

这种性质叫beautiful arrangement，定义是对任意 :math:`1 \leq i \leq N` 有下列任意一个条件满足

-   :math:`a_i \mod i`
-   或 :math:`i \mod a_i`
"""

from typing import *

class Solution:
    def countArrangement(self, N: int) -> int:
        