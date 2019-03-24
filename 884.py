"""
列出两个array里面不共有、且只出现了一次的元素。

所以这个题的题目很有迷惑性，只说了一个条件，实际上还要求这个元素只出现一次。

1.  得到A中出现过的元素的集合、直方图
2.  得到B中出现过的元素的集合、直方图
3.  遍历每一个A或B中出现过的元素，看是否符合要求，符合要求就放入池子里
"""

from typing import *

import collections

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # wordsInA = set(A.split())
        # wordsInB = set(B.split())
        # words = wordsInA.union(wordsInB)
        counterA = collections.Counter(A.split())
        counterB = collections.Counter(B.split())
        res = []

        for v in (counterA + counterB).keys():
            if (counterA[v] == 1 and counterB[v] == 0) or (counterA[v] == 0 and counterB[v] == 1):
                res.append(v)

        return res

s = Solution()
assert s.uncommonFromSentences("apple apple", "banana") == ["banana"]
assert s.uncommonFromSentences("this apple is sweet", "this apple is sour")
assert s.uncommonFromSentences("s z z z s", "s z ejt") == ["ejt"]