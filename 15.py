r"""
.. default-role:: math

著名的3sum。给一个array，问其中有哪些三个数的组合的和是0，每个数字在每个组合里只能出现一次，组合不能重复，比如 ``1, 1, 2`` 和 ``1, 2, 1`` 算作是同一个组合。

即给一个序列 `\{a_n\}` ，求集合

.. math::

    \{(a_i, a_j, a_k) | 0 \geq i, j, k \geq n - 1, i \neq j \neq k, a_i \geq a_j \geq a_k\}

因为已经解决过2sum问题，所以很容易 [#]_ 想到可以利用2sum的代码来解决3sum问题。2sum中我们已经解决过 ``a + b == target`` 的问题，现在又来了一个 ``c`` ，变成了 ``a + b + c == target`` ，做一个简单的移项，变成 ``a + b == target - c`` ，所以做法也就出来了：遍历array中的每个数字 ``c`` ，把 ``target - c`` 作为2sum搜索的目标值。

2sum搜索的时候可以只搜索当前数字后面的数字，可以快一点（降低前面的常数项但不降低阶数）。

.. [#] 大概吧……
"""

from typing import *

import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        nums = sum(([k] * min(3, v) for k, v in counter.items()), []) # 先简单过滤一下，把每个元素出现的次数限制在3及以下，因为不允许组合重复，所以元素出现次数太多并没有意义
        res = set() # 存结果

        for i, v in enumerate(nums): # 遍历array中的每个数字
            combinationsSumToNegativeC = self.twoSum(nums[i + 1: ], - v) # 以target - c为目标值，从当前数字后面开始搜索所有a + b == target - c的(a, b)组合
            res.update(tuple(sorted((v, ) + combination)) for combination in combinationsSumToNegativeC) # 处理重复

        return list(map(list, res))

    def twoSum(self, nums: List[int], target: int) -> "Set[Tuple[int, ...]]": # 先解决2sum问题。这个函数输出所有加和是target的组合。组合不重复，数字可以重复。
        seen = set() # 所有已经见过的数
        res = set() # 存所有加和是target的组合，用set可以保证不重复

        for number in nums: # 遍历一遍，所以复杂度O(n)
            if target - number in seen: # 看前面有没有数字和当前这个数字加起来是target
                res.add(tuple(sorted([number, target - number]))) # 如果是，就加入到res里，为了不重复，先做个排序、变成tuple之后再加入到res里
            seen.add(number) # 不管有没有遇到互补数，都要加入到seen里

        return res

# s = Solution()
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
# print(s.threeSum([0] * 10000))