"""
在array里找到能够使 :math:`a_i & a_j & a_k = 0` 成立的所有 :math:`i, j, k` 。

:math:`i, j, k` 没有任何条件，意味着可以重复、可以交换位置。

有两件事情需要注意

-   对任意满足 ``a & b & c == 0`` 的a, b, c来说，必有 ``a & b == 0`` 或 ``a & c == 0`` 或 ``b & c == 0``
-   对任意x，有 ``x & 0 == 0``

所以只要

1.  先把所有的0找出来，算出所有含0的组合数量

    假设array里面有n个元素，其中含有k个0，那么对于每个0来说都有三种

2.  排除掉0，算出所有不含0的组合数量
"""

from typing import *

import collections

class Solution:
    def countTriplets(self, A: List[int]) -> int:
        counter = collections.Counter(A)
