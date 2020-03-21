"""
定义 `n` 正整数的power为把 `n` 变成1的需要经过的状态数

-   如果 `n` 是偶数， `n` 可以除以2
-   如果 `n` 是奇数， `n` 要变成 `3n + 1`

比如给3 ，把3变成1需要经过7个状态（算上初始状态）

::

    3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

现在把 `[l, h]` 区间里面所有的数放在一起，按power从小到大排序，如果power相同，按数字本身排序。这样排好序之后，第 `k` 小的数字是哪个？

排序这一步好像没办法变快，所以想办法把计算power这一步变快。马上就能想到用cache，把 `[1, 1000]` 以内所有的数字的power全部都事先算出来，这样取power的时候就不用计算了，直接查表就行了。
"""

from typing import *

import functools

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        for i in range(1, 1001): # 刷cache
            self.steps(i)

        res = sorted((i for i in range(lo, hi + 1)), key=lambda i: (self.steps(i), i))

        return res[k - 1]

    @functools.lru_cache(None)
    def steps(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            if n % 2 == 0:
                return 1 + self.steps(n // 2)
            else:
                return 1 + self.steps(3 * n + 1)

s = Solution()
print(s.getKth(12, 15, 2)) # 13
print(s.getKth(1, 1, 1)) # 1
print(s.getKth(7, 11, 4)) # 7
print(s.getKth(10, 20, 5)) # 13
print(s.getKth(10, 1000, 777)) # 570