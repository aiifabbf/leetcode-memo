"""
array里面的每个数字是否出现了独一无二次？

比如 ``[1, 2, 2, 1, 1, 3]`` 里面

-   ``1`` 出现了3次
-   ``2`` 出现了2次
-   ``3`` 出现了1次

``1, 2, 3`` 出现的次数都是不同的。

很简单，用Counter数一下，再看一下 ``Counter.values()`` 是否有重复元素就好了。把 ``Counter.values()`` 分别转换成list和set，然后比较一下长度，如果长度不一致，说明出现了 ``Counter.values()`` 里面出现了重复元素。
"""

from typing import *

import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr) # Counter数一下
        return len(set(counter.values())) == len(list(counter.values())) # 如果set和list长度不同，说明list里面有重复元素