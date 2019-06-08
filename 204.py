r"""
小于n的所有自然数里有多少个素数？

用筛法 [#]_ 复杂度可以做到 :math:`O(n \ln n)` 。

.. [#] https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

from typing import *

import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        else:
            isPrime = [True] * n # isPrimes[i]用来标记i是不是素数。一开始假定全部都是素数
            isPrime[0] = False
            isPrime[1] = False # 0和1不考虑

            for i in range(2, math.floor(math.sqrt(n)) + 1): # 从2开始遍历
            # for i in range(2, n): # 其实不需要从2到n，到ceil(sqrt(n))就够了。为什么我也没想通
                if isPrime[i] == True: # 发现i是素数

                    for j in range(i * i, n, i): # 遍历k * i
                    # for j in range(i * 2, n, i): # 这里也不需要从i * 2开始，直接从i^2开始就可以了。为什么我也没想通
                        isPrime[j] = False # 把k * i标记为非素数

            return sum(isPrime)

# s = Solution()
# assert s.countPrimes(10) == 4
# assert s.countPrimes(100) == 25
# assert s.countPrimes(49979) == 5130