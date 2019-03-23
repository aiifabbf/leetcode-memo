"""
给你一个array，问你能否找到一种方法，把这个array分成一些大小相同的subarray（不一定要连续），使得这些subarray满足两个条件

-   subarray里至少要有2个元素
-   同一个subarray里的所有元素相等

第一个条件很容易做，就是用一个Counter去数array，然后看出现次数最小的元素出现了多少次，如果出现的次数小于2，直接False。

问题是第二个条件不太容易做，而且有很多陷阱，比如 ``[1, 1, 1, 1, 2, 2, 2, 2, 2, 2]`` 这里面有4个1、6个2，如果贪心，把4个1分成一组，就会发现6个2没办法分组了，所以这个时候只能把4个1拆成2个1一组，才能把6个2拆成2个2三组。所以这里要用到频次的最大公因数。

思路是用Counter去数array里每个元素出现的频次，再求这些频次的共同最大公因数（GCD），看这个最大公因数是否大于等于2。
"""

from typing import *

import collections
import fractions
import functools

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) >= 2:
            counter = collections.Counter(deck)
            return functools.reduce(fractions.gcd, counter.values()) >= 2
        else:
            return False

s = Solution()
assert s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])
assert not s.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3])
assert not s.hasGroupsSizeX([1])
assert s.hasGroupsSizeX([1, 1])
assert s.hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) # 这个case是可以的……只要分的时候每组牌堆分2个。