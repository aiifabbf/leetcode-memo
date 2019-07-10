r"""
.. default-role:: math

求出一个array的所有累加和在 ``[lower, upper]`` 区间内的substring（要连续）的个数。

即求集合

.. math::

    \{(i, j) | \sum_{k = i}^{j - 1} a_k \in [l, u], 0 \leq i < j \leq n\}

的大小。

形式和795题很像，795题是最大值，这里是和。

还是积分的做法。做完积分之后，遍历每个积分值，假设当前积分值是 `S_i` ，然后从当前积分值往后面找，看后面有多少个积分值是 `S_i + l, S_i + l + 1, ..., S_i + u - 1, S_i + u` 的项，有几个就说明有这么多个substring的和是在 `[l, u]` 区间内。

当然如果就是这样找的话，整个复杂度还是 `O(n^2)` ，所以要想办法快速找到当前积分项后有多少个，这就需要用到 ``Counter`` 。做完积分之后，先用 ``Counter`` 统计一下每个积分值出现的次数。遍历到当前积分项的时候，把 ``Counter`` 中当前积分项的值出现的次数减一，然后就可以直接在 `O(1)` 复杂度下，判断当前项的后面是否存在某个值的积分项了。

这样最终复杂度是 `O(n \times (u - l + 1))` 。
"""

from typing import *

import itertools
import collections

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # integral = [0] + list(itertools.accumulate(nums)) # 这样子nums[i: j]的和就是integral[j] - integral[i]
        # count = 0

        # for i in range(0, len(nums)): # i的范围是[0, 1, ..., n-1]

        #     for j in range(i + 1, len(nums) + 1): # j的范围是[i+1, i+2, ..., n]
        #         if lower <= integral[j] - integral[i] <= upper:
        #             count += 1

        # return count
        # 暴力做法不可取

        integrals = [0] + list(itertools.accumulate(nums))
        counter = collections.Counter(integrals)
        count = 0

        for v in integrals:
            counter[v] -= 1

            for delta in range(lower, upper + 1):
                count += counter[v + delta]

        return count

# s = Solution()
# print(s.countRangeSum([-2, 5, -1], -2, 2))