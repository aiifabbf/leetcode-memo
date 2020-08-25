"""
.. default-role:: math

实现带权采样

大致原理是把给你的权重array ``weights`` 看作是非归一化的概率密度函数，然后积分/前缀和算出非归一化的概率分布函数 ``cdf`` ， ``cdf[i + 1] - cdf[i]`` 是取第 `i` 个元素的权重。

采样的时候，在 `[0, \sum w)` 区间里按均匀分布随机取一个整数 `k` ，再去 ``cdf`` 里面找一个 ``cdf[i]`` 使得 `k` 在 ``[cdf[i], cdf[i + 1])`` 区间里。此时 `i` 就是最终要返回的样本。

举个例子，比如权重是 ``[3, 14, 7, 1]`` ，那么非归一化概率分布函数是

::

    0, 3, 17, 24, 25

第0个区间是 `[0, 3) ，第1个区间是 `[3, 17)` ，第2个区间是 `[17, 24)` ，第3个区间是 `[24, 25)` 。

现在在 `[0, 25)` 里均匀采样，假设采样得到的是2，2正好在 `[0, 3)` 区间里，所以样本是0。假设采样得到的是10，10正好在 `[3, 17)` 区间里，所以样本是1。假设采样得到24，24在 `[24, 25)` 里，所以样本是3。

所以还是二分搜索的套路。

.. 更详细的推导在497的注释里。
"""

from typing import *

import itertools
import random


class Solution:

    def __init__(self, w: List[int]):
        self.cdf = [0] + list(itertools.accumulate(w)) # 概率分布函数

    def pickIndex(self) -> int:
        k = random.randint(0, self.cdf[-1] - 1) # 在[0, sum(weights))里按均匀分布取一个数

        # 然后用二分找到这个数属于第几个区间，如果k属于[a_i, a_{i + 1})，那么应该返回i
        left = 0
        right = len(self.cdf)

        while left < right:
            middle = (left + right) // 2
            if k > self.cdf[middle]:
                left = middle + 1
            elif k < self.cdf[middle]:
                right = middle
            else: # 相等的时候，必须往左看，不能往右看，因为可能会有权重是0的数字，如果往右看了的话，会永远取右边的数字
                right = middle

        if self.cdf[left] == k:
            return left
        else:
            return left - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()