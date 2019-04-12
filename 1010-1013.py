"""
找到一个array里所有加起来是60的倍数的数对（先后只算一次，重复也要算），即确定一个array的 :math:`\{(i, j) | a_i + a_j \pmod 60 = 0, 0 \leq i < j \leq n - 1\}` 的大小。

最简单的做法就是暴力搜索，复杂度 :math:`O(n^2)` ，试了下好像是过不去的。

根据two sum还有447题想到了一个HashMap的做法，复杂度应该是 :math:`O(n)` 吧……
"""

from typing import *

import collections
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = collections.Counter()
        pairCount = 0

        for i in time:
            if i % 60 == 0: # 这里我第一次出问题了，因为如果本身这个元素就是60的倍数的话，是永远找不到60 - i % 60的，也就是说counter里面不可能出现60这个key，只会出现0这个key。所以对于本身就60的倍数的元素要拎出来考虑。
                pairCount += counter[0]
            else:
                # if 60 - i % 60 in counter: # 这个好像是不用判断的……因为counter会给你处理好不存在的情况
                pairCount += counter[60 - i % 60]
            counter[i % 60] += 1

        return pairCount

s = Solution()
assert s.numPairsDivisibleBy60([30, 20, 150, 100, 40]) == 3
assert s.numPairsDivisibleBy60([60, 60, 60]) == 3