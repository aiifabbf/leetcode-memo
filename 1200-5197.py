r"""
.. default-role:: math

给一个全是数字的array `\{a_k\}` ，找到所有 `(a, b), a < b` 使得 `b - a` 正好是array里两个数字的最小绝对差（就是任意从array里面选两个不相等的数字，它们的差的绝对值的最小值）

.. math::

    b - a = \min\{|x - y| | x, y \in \{a_k\}, x \neq y\}

很简单，先给array从小到大排序，变成 ``\{a'_k\}` ，右边式子的值就是

.. math::

    \min\{a'_k - a'_{k - 1}\}

记为 `d` 。

然后再用一次2sum，遍历一遍array，遍历到 `a_k` 的时候，看看 `a_k - d` 之前有没有见过，如果见过，就把 `(a_k - d, a_k)` 加入到结果集合里面。

排序的复杂度是 `O(n \ln n)` ，一次2sum的复杂度是 `O(n)` ，所以总的复杂度应该是 `O(n \ln n)` 。
"""

from typing import *

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr) # 先给array排序
        minimumAbsoluteDifference = float("inf") # 记录array中的最小绝对差

        for i, v in enumerate(arr[1: ], 1):
            minimumAbsoluteDifference = min(minimumAbsoluteDifference, abs(v - arr[i - 1])) # 求出min(a[i] - a[i - 1])

        res = [] # 结果集合
        seen = set() # 记录前面见过的数字

        for v in arr: # 遍历一遍array，用一次2sum
            if v - minimumAbsoluteDifference in seen: # 看看a[k] - d之前有没有见过，如果见过
                res.append([v - minimumAbsoluteDifference, v]) # 加入到结果集合里面
            seen.add(v) # 把a[k]加入到前面见过的数字集合里面

        return res

# s = Solution()
# print(s.minimumAbsDifference([4, 2, 1, 3]))
# print(s.minimumAbsDifference([1, 3, 6, 10, 15]))
# print(s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))