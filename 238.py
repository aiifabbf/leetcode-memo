"""
.. default-role:: math

给一个array，对于每个数，算出整个array排除自己之后得到的subsequence的积。

很简单，有点像prefix sum前缀和，这里是prefix product前缀积2333。

Rust版的没有考虑 `O(1)` ，这里考虑了。很容易想到的。

先占用输出空间（输出空间不算临时空间的），把 ``productAfter[i]`` 全部算出来。 ``productAfter[i]`` 表示第 `i` 个数之后的累积。

然后一边遍历，一边算 ``productBefore[i]`` 。 ``productBefore[i]`` 表示第 `i` 个数之前的累积。算出来之后直接和 ``productAfter[i + 1]`` 相乘，覆盖掉 ``productAfter[i]`` ，因为反正之后也用不到了。
"""

from typing import *

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAfter = [1]

        for v in reversed(nums):
            productAfter.append(productAfter[-1] * v)

        productAfter.reverse()

        productBefore = 1 # 其实不需要得到每个productBefore[i]，只需要前一项就够了

        for i, v in enumerate(nums):
            productAfter[i] = productBefore * productAfter[i + 1] # 一边遍历一遍覆盖
            productBefore = productBefore * v

        return productAfter[: -1] # 最后一个是1，不用返回