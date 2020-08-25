"""
.. default-role:: math

一开始array全是0，每一步可以做下面两个操作中的其中一个

-   要么选1个数，加1
-   要么把array里每个数都乘以2

最少需要多少步才能把全0的array变成目标array？

比如从 ``[0, 0]`` 到 ``[1, 5]`` 最少需要5步

1.  ``[0, 0] -> [0, 1]``
2.  ``[0, 1] -> [0, 2]``
3.  ``[0, 2] -> [0, 4]``
4.  ``[0, 4] -> [0, 5]``
5.  ``[0, 5] -> [1, 5]``

可以反过来想，如果array里有一个奇数 `k` ，它只可能是由 `k - 1` 这个偶数加1而来。如果array里有个偶数 `k` ，它最好是通过 `k / 2` 这个数乘2得到，而不是通过 `k / 2` 一个一个加1而来，因为这样更快。

所以模拟一下整个过程，每一轮先找到array里所有的奇数，然后把它们每个都减1，这样array里就只剩偶数了，再一次全部除以2。

.. 这算是greedy吗，我也不知道怎么证明……
"""

from typing import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0  # 操作了多少次

        while True:

            for i in range(len(nums)):
                v = nums[i]
                if v % 2 != 0:  # 发现一个奇数
                    nums[i] = nums[i] - 1  # 它只可能是由偶数加1而得
                    res += 1

            if not any(v != 0 for v in nums):  # 如果所有数字都变成0了
                break  # 说明结束了

            # 到这里能保证array里面只有偶数，这时候全部除以2，算一次操作
            for i in range(len(nums)):
                nums[i] = nums[i] // 2

            res += 1

        return res


s = Solution()
print(s.minOperations([1, 5]))  # 5
print(s.minOperations([2, 2]))  # 3
print(s.minOperations([4, 2, 5]))  # 6
print(s.minOperations([3, 2, 2, 4]))  # 7
print(s.minOperations([2, 4, 8, 16]))  # 8
