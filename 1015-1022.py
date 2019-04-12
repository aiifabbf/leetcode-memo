"""
找到十进制表示里只含有 ``1`` 的（比如111、111111）、且能整除K的最小正整数。
"""

from typing import *

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0:
            return -1

        for i in range(1, 10**5):
            number = int("1" * i)
            if number % K == 0:
                print(number, i)
                return i
        else:
            return -1

s = Solution()
assert s.smallestRepunitDivByK(1) == 1
assert s.smallestRepunitDivByK(2) == -1
assert s.smallestRepunitDivByK(3) == 3
assert s.smallestRepunitDivByK(5) == -1
assert s.smallestRepunitDivByK(5367) == 1788