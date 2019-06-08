"""
最长的非公共subsequence（不一定连续）？

这题完全不知所云。评分也很差，不管了。
"""

from typing import *

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a), len(b))