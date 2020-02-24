"""
.. default-role:: math

给一个数字 `n` ，返回一对数 `a, b`，使得 `ab` 恰好等于 `n + 1` 或者 `n + 2` ，同时 ``|a - b|`` 要尽可能小。

那很简单，对 `n + 1` 算一次得到一对数、对 `n + 2` 算一次得到一对数，然后取差的绝对值小的那一对就好了。
"""

from typing import *

import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a = self.divisors(num + 1) # 算一下n + 1
        b = self.divisors(num + 2) # 算一下n + 2
        return sorted(min([a, b], key=lambda v: abs(v[1] - v[0]))) # 取差的绝对值小的那对

    def divisors(self, n: int) -> List[int]: # 计算a, b使得a * b = n同时abs(a - b)尽可能小
        res = [1, n]

        for i in range(1, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                res = [i, n // i]

        return res

s = Solution()
print(s.closestDivisors(8)) # 3, 3
print(s.closestDivisors(123)) # 5, 25
print(s.closestDivisors(999)) # 40, 25