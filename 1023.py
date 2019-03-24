"""
1到N的每一个数字的二进制表示是否是S的substring？
"""

from typing import *

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for v in range(1, N + 1):
            if bin(v)[2: ] not in S:
                return False
        else:
            return True

s = Solution()
assert s.queryString("0110", 3)
assert not s.queryString("0110", 4)
assert not s.queryString("110101011011000011011111000000", 15)