r"""
.. default-role:: math

给一组二维点 `(x_i, y_i)` ，问有多少个点对满足 `x_i = y_i, x_j = y_j` 或 `x_i = y_j, x_j = y_i` ，并且 `i < j` 。

很简单，先给每个点排序，然后用 ``Counter`` 统计每个点出现的次数，如果同一个点出现 `n` 次且 `n \geq 2` ，那么这个点可以组成 `n (n - 1) / 2` 个点对。

-   假设出现了2次，那么

    -   1, 2组成点对

    总共1对。

-   假设出现了3次，那么

    -   1, 2组成点对
    -   1, 3组成点对
    -   2, 3组成点对

    总共3对。

-   假设出现了4次，那么

    -   1, 2
    -   1, 3
    -   1, 4
    -   2, 3
    -   2, 4
    -   3, 4

    总共6对。

-   ...

找下规律，发现是增一数列求和。
"""

from typing import *

import collections

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = collections.Counter(map(lambda v: tuple(sorted(v)), dominoes)) # 先逐个排序，然后变成tuple，这样才能被hash。然后统计每个点出现的频次
        return sum(v * (v - 1) // 2 for k, v in counter.items() if v >= 2) # 如果一个点出现了n次且n >= 2，那么这个点可以组成n * (n - 1) / 2个符合题意的点对

# s = Solution()
# print(s.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))