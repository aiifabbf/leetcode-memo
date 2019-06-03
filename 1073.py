"""
给两个-2进制的数字，以list形式给出每一位，问它们的和，同样以list形式给出每一位。

直接用了1017里面的int转-2进制的函数。
"""

from typing import *

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        number1 = self.listToInt(arr1) # list变成int
        number2 = self.listToInt(arr2) # list变成int
        return list(map(int, list(self.baseNeg2(number1 + number2))))

    def listToInt(self, l: list) -> int: # 把list变成int
        res = 0

        for i, v in enumerate(reversed(l)):
            res += v * (-2) ** i

        return res

    def baseNeg2(self, N: int) -> str: # 摘自1017，int转list
        if N == 0:
            return "0"

        res = []

        while N != 0:
            if N % 2 == 0: # N是偶数
                remainder = 0 # r一定是0
                N = - (N // 2) # 算出d，作为下一轮新的N
            else: # N是奇数
                remainder = 1 # r一定是1
                N = (N - 1) // -2 # 算出d，作为下一轮新的N
            res.append(str(remainder)) # 记录r

        return "".join(res[:: -1]) # 结果是r的倒序

# s = Solution()
# print(s.addNegabinary([1, 1, 1, 1, 1], [1, 0, 1])) # [1, 0, 0, 0, 0]