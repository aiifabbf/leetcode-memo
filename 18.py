"""
.. default-role:: math

不是特别著名的4sum。

其实就是在3sum的基础上再套一层，所以可想而知可以像 ``5sum, 6sum, 7sum, ...`` 套无数层。但只有第一层 ``2sum`` 的复杂度可以从 `O(n^2)` 降低到 `O(n)` ，所以 ``ksum`` 的复杂度是 `O(n^{k - 1})` 。

思路和3sum利用2sum完全一样，也是利用3sum的结果。所以可以先看一看15题3sum的 `注解 <./15.py>`_ 。

3sum解决的问题是 ``a + b + c == target`` ，现在要解决 ``a + b + c + d == target`` 的问题，那么就做一次移项，变成 ``a + b + c == target - d`` 。可以看到形式和3sum一样了，只是这里多了 ``d`` 这个变量。

所以做法是：遍历array里每一个数字 ``d`` ，以 ``target - d`` 为目标，从当前数字后面开始跑3sum，找所有和是 ``target - d`` 的组合。
"""

from typing import *

import collections

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(nums)
        nums = sum(([k] * min(4, v) for k, v in counter.items()), [])
        res = set() # 和3sum里一样，先过滤一下，把每个元素出现的次数都限制在小于等于4，因为不允许组合重复，所以元素出现次数多没有意义，徒增复杂度

        for i, v in enumerate(nums): # 遍历array里的每个数字
            res.update(tuple(sorted(combination + (v, ))) for combination in self.threeSum(nums[i + 1: ], target - v)) # 以target - v为目标值、从v后面的数字开始找和为target - v的组合

        return list(map(list, res))

    def threeSum(self, nums: List[int], target: int) -> "Set[Tuple[int, ...]]": # 解决4sum之前不妨先解决3sum问题
        res = set()

        for i, v in enumerate(nums):
            res.update(tuple(sorted(combination + (v, ))) for combination in self.twoSum(nums[i + 1: ], target - v))

        return res

    def twoSum(self, nums: List[int], target: int) -> "Set[Tuple[int, ...]]": # 解决3sum问题之前不妨先解决2sum问题
        seen = set()
        res = set()

        for v in nums:
            if target - v in seen:
                res.add(tuple(sorted([v, target - v])))
            seen.add(v)

        return res

# s = Solution()
# print(s.fourSum([1, 0, -1, 0, -2, 2], 0))