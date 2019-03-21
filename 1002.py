"""
得到几个字符串共同出现的字符。要考虑重复。

我的思路是先逐个给每个字符串做一个频次直方图，然后再取这些直方图共同的交集 [#]_ 。

.. [#] 就是如果这一个元素只在一个直方图里出现，就不取；如果这个元素在两个直方图里都出现了，就取它在两个字符串里出现频次的最小值。

评论区看到一个 神仙__ 也是这么做的，但是一行就搞定了……原来 ``collections.Counter`` 自带有 ``__and__()`` 方法，直接 ``counter1 & counter2`` 就可以取交集。而且 ``collections.Counter`` 还自带有一个 ``.elements()`` 方法，直接就可以按次数输出所有的元素……简直是贴心得不行。

我原来以为我已经挺熟悉 ``Counter`` 了，没想到……好了滚去看文档了。

__ https://leetcode.com/problems/find-common-characters/discuss/247560/Python-1-line
"""

from typing import *

import collections
import functools

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if A:
            counter = functools.reduce(self.counterIntersection, map(collections.Counter, A))
            return sum([[i] * v for i, v in counter.items()], [])

        else:
            return []
        # return list(functools.reduce(collections.Counter.__and__, map(collections.Counter, A)).elements()) # 神仙做法……平常还是别这么写了吧

    def counterIntersection(self, p: collections.Counter, q: collections.Counter) -> collections.Counter: # 取两个直方图的交集
        commonItem = set(p).intersection(q)
        counter = collections.Counter()

        for v in commonItem:
            counter[v] = min(p[v], q[v])

        return counter