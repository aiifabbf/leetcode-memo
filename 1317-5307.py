"""
.. default-role:: math

给一个正整数 `n` ，找到两个正整数 `a, b` 使得

-   `a + b = n`
-   `a, b` 的十进制表示里不含有0

我的做法是先找出 `[1, n)` 里所有十进制表示不含有0的数字，然后跑一下类似two sum的东西。
"""

from typing import *

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        allNoZeroIntegers = set(i for i in range(1, n) if "0" not in str(i)) # [1, n)中所有十进制表示不含有0的数字

        for v in allNoZeroIntegers: # 遍历每个数字a
            if n - v in allNoZeroIntegers: # 如果n - a的十进制表示不含0
                return [v, n - v] # 那么找到了

s = Solution()
print(s.getNoZeroIntegers(2)) # [1, 1]
print(s.getNoZeroIntegers(11)) # [2, 9]