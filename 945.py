"""
.. default-role:: math

给一个array，每次可以选择array里的某个元素加1，问最少加多少次，可以使得array里面的每个元素都只出现一次。

数据规模是40000，应该是在暗示一种 `O(n)` 或者 `O(n \ln n)` 做法。

虽然不知道这样做为什么能work [#]_ ，按直觉来做就能过

1.  给array排序
2.  遍历array里面的每个元素，如果发现当前元素比前面一个元素小或者相等，就把当前元素抬高到比前面一个元素恰好大1个单位的位置

.. [#] 可能是因为这道题只能+1不能-1。
"""

from typing import *

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        sortedArray = sorted(A) # 先排序
        res = 0

        for i in range(1, len(sortedArray)): # 因为要一边遍历一遍修改，所以用i
            if sortedArray[i] <= sortedArray[i - 1]: # 如果发现当前元素比前面一个元素小或者相等
                res += sortedArray[i - 1] + 1 - sortedArray[i]
                sortedArray[i] = sortedArray[i - 1] + 1 # 把当前元素抬高到比前面一个元素大1的位置

        # print(sortedArray)
        return res

# s = Solution()
# print(s.minIncrementForUnique([1, 2, 2])) # 1
# print(s.minIncrementForUnique([3, 2, 1, 2, 1, 7])) # 6