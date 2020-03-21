"""
.. default-role:: math

给两个array ``a, b`` ，问 ``a`` 中有多少个元素 ``a[i]`` 满足“对于任意 ``b[j]`` 都不存在 `|a_i - b_j| \leq d` ”？

非常拗口，看不懂。一看数据规模只有500，那么暴力好了。
"""

from typing import *


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0

        for v in arr1:
            if not any(abs(v - w) <= d for w in arr2): # 直接把题目的意思抄下来
                res += 1

        return res


s = Solution()
print(s.findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))  # 2
print(s.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3))  # 2
print(s.findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6))  # 1
