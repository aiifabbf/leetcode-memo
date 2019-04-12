"""
输出一个string里面、所有是另一个字符串p的anagram [#]_ 的substring的起始下标

.. [#] 所谓anagram就是直方图完全相同的两个substring，就是两个string中，出现的字符的种类完全一样、并且每个字符在两个string中出现的次数也完全一样多。
"""

from typing import *

import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lengthOfP = len(p)
        lengthOfS = len(s)
        if lengthOfP > lengthOfS:
            return []
        else:
            res = []
            counterP = collections.Counter(p)
            counterS = collections.Counter(s[0: lengthOfP]) # 初始条件
            if counterP == counterS:
                res.append(0)

            for i in range(1, lengthOfS - lengthOfP + 1): # 判断[i, i + 1, i + 2, ..., i + lengthOfP - 1]之间的substring
                # counterS = collections.Counter(s[i: i + lengthOfP])
                # 这样每次都重新数一遍肯定是不行的，考虑缓存加速
                counterS[s[i - 1]] -= 1 # 把前一个字符删掉
                counterS[s[i + lengthOfP - 1]] += 1 # 加入最后一个字符
                if + counterS == + counterP: # +号的目的是去掉非正数
                    res.append(i)

            return res

# s = Solution()
# assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
# assert s.findAnagrams("abab", "ab") == [0, 1, 2]