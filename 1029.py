r"""
给一个只含0和1的array，问 :math:`(a_0 a_1 a_2 ... a_{i})_2, 0 \leq i \leq n - 1` 能否被5整除。

这个题用其他不自带bigint的语言来说应该挺难的……然而py就没有这个问题了。
"""

from typing import *

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        # buffer = ""
        number = 0

        for v in A:
            # buffer += str(A[i])
            # number = int(buffer, 2)
            number = (number << 1) + v # 注意运算符优先级……
            if number % 5 == 0:
                res.append(True)
            else:
                res.append(False)

        return res

# s = Solution()
# print(s.prefixesDivBy5([0, 1, 1]))
# print(s.prefixesDivBy5([1, 1, 1]))