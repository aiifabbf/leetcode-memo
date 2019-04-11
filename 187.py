"""
找出string里所有重复出现了多次的长度为10的substring（要连续）。

马上就想到用 ``set`` 来存所有出现过的substring了。这样做只扫描了一遍字符串，复杂度应该是 :math:`O(n)` 。
"""

from typing import *

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        else:
            seen = set() # 存所有出现过的substring
            res = set() # 存出现了多次的substring

            for i in range(0, len(s) - 10 + 1):
                string = s[i: i + 10]
                if string in seen: # 这个操作应该是O(1)
                    res.add(string)
                else:
                    seen.add(string)

            return list(res)