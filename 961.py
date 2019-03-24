"""
获得一个大小为2n的array里面出现了n次的元素。

我直接就想到了Counter做法，但是题目其实还有额外信息，就是除了这个出现了n次的元素以外，其他元素都是只出现一次的。
"""

from typing import *

import collections

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # length = len(A)
        # counter = collections.Counter(A)
        # return [i for i, v in counter.items() if v == length // 2][0]
        # 一改：利用一下其他元素只出现一次的性质。
        seen = set()

        for v in A:
            if v not in seen:
                seen.add(v)
            else:
                return v