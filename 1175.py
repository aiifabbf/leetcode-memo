r"""
.. default-role:: math

给一个数字 `n` ，把所有的素数放在下标（下标从1开始）是素数的格子里，问总共有多少种组合。

比如 ``1, 2, 3, 4, 5`` ，其中 ``2, 3, 5`` 是素数，要放到下标是素数的格子里，那么总共有多少种方法？

首先先排好 ``2, 3, 5`` ，总共有 `A_3^3` 种排列方式；剩下的 ``1, 4`` 总共有 `A_2^2` 种排法，所以一共是

.. math::

    A_3^3 \times A_2^2 = 3! 2! = 12

种排法。

::

    1 2 3 4 5
      ^ ^   ^--素数下标的格子
    ---------


其实就是统计 `[1, n)` 中素数的个数、加上一个简单的组合数学问题。
"""

from typing import *

import math

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primeCount = self.countPrimes(n + 1) # 先统计[1, n]中素数的个数。n - primeCount就是非素数
        return (math.factorial(n - primeCount) * math.factorial(primeCount)) % (10**9 + 7)
        
    def countPrimes(self, n: int) -> int: # 统计[1, n)中素数的个数
        if n <= 2:
            return 0
        else:
            isPrime = [True] * n
            res = 0

            for i in range(2, n):
                if isPrime[i] == True:
                    res = res + 1

                    for j in range(2 * i, n, i):
                        isPrime[j] = False

            return res

# s = Solution()
# print(s.numPrimeArrangements(5)) # 12
# print(s.numPrimeArrangements(100)) # 682289015