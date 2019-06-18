"""
把array里所有出现的0都重复两次，再截断成原array的长度。
"""

from typing import *

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res = []

        for v in arr:
            if v == 0: # 如果遇到0
                res.append(0)
                res.append(0) # 加两次0
            else:
                res.append(v)
            if len(res) >= len(arr): # 加完之后如果发现数组的长度大于等于原array的长度
                arr[:] = res[: len(arr)] # 截断
                return

        # 也有可能array里没有0，所以长度不变
        arr[:] = res[: len(arr)]
        return

# s = Solution()

# arr = [1, 0, 2, 3, 0, 4, 5, 0]
# s.duplicateZeros(arr)
# print(arr)

# arr = [1, 2, 3]
# s.duplicateZeros(arr)
# print(arr)

# arr = [0]
# s.duplicateZeros(arr)
# print(arr)

# arr = []
# s.duplicateZeros(arr)
# print(arr)