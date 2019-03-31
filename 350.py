"""
两个array（含重复元素）的交集（也要包含重复元素）

两个array先做一下直方图，然后按元素取两个直方图里的最小值。python直接可以用两个 ``Counter`` 相与。

.. note:: ``collections.Counter`` 真的有非常非常多的神奇用法。

    .. code:: python

        >>> c = Counter(a=3, b=1)
        >>> d = Counter(a=1, b=2)
        >>> c + d                       # add two counters together:  c[x] + d[x]
        Counter({'a': 4, 'b': 3})
        >>> c - d                       # subtract (keeping only positive counts)
        Counter({'a': 2})
        >>> c & d                       # intersection:  min(c[x], d[x]) # doctest: +SKIP
        Counter({'a': 1, 'b': 1})
        >>> c | d                       # union:  max(c[x], d[x])
        Counter({'a': 3, 'b': 2})

    上面是从 官方文档_ 里摘下来的。

    .. _官方文档: https://docs.python.org/3/library/collections.html#collections.Counter
"""

from typing import *

import collections

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        counter = counter1 & counter2

        return sum(([i] * v for i, v in counter.items()), [])

# s = Solution()
# print(s.intersect([1, 2, 2, 1], [2, 2]))
# print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))