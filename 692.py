"""
返回出现频率最高的K个词。如果同时有多个词出现频率一样大，返回lexicography最小的那个。
"""

from typing import *

import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        return sorted(counter.keys(), key=lambda v: (- counter[v], v))[: k]