"""
.. default-role:: math

凑硬币。给一组面值，每种面值可以用无限次，问最少用多少个硬币可以凑出数额

类似518，只不过518要计算的是种类个数，这一题要算的是最少用多少个硬币。

详细解释在Rust版里。
"""

from typing import *

import functools


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # @functools.lru_cache(None)
        # def f(j: int, c: int) -> int:
        #     # print(j, c)
        #     if j == 0 and c == 0:
        #         return 0
        #     elif j == 0 and c != 0:
        #         return -1
        #     else:
        #         res = float("inf")

        #         for n in range(0, 10**9):
        #             if c - n * coins[j - 1] >= 0:
        #                 remain = f(j - 1, c - n * coins[j - 1])
        #                 if remain != -1:
        #                     res = min(res, n + remain)
        #             else:
        #                 break

        #         if res != float("inf") :
        #             return res
        #         else:
        #             return -1

        # return f(len(coins), amount)
        # f(j, c)过不了

        @functools.lru_cache(None)
        def f(c: int) -> int: # 凑出c元钱最少需要多少个硬币
            if c == 0:
                return 0
            else:
                return min((1 + f(c - v) for v in coins if c - v >= 0), default=float("inf"))

        res = f(amount)
        if res == float("inf"):
            return -1
        else:
            return res


s = Solution()
print(s.coinChange([1], 2)) # 2
print(s.coinChange([1, 2, 5], 11)) # 3
print(s.coinChange([2], 3)) # -1
print(s.coinChange([216, 94, 15, 86], 5372)) # 26
print(s.coinChange([186, 419, 83, 408], 6249)) # 20
print(s.coinChange([346, 29, 395, 188, 155, 109], 9401)) # 26
