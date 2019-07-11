"""
.. default-role:: math

输出一个奇怪的数列 [#]_ 的第 `n` 项。数列的第一项是1，第二项开始，每项都是数前面一项里面，每个连续的重复出现的数字出现的次数+这个数字。

比如因为第一项是 ``1`` ，是1个1，所以第二项是 ``11`` ；因为第二项是2个1，所以第三项是 ``21`` ；因为第三项是1个2和1个1，所以第四项是 ``1211`` ……

因为没有通项公式，那就按题目要求做吧。讨论里面我好像也没有看到比直接做复杂度更低的做法。

.. [#] 这个数列是 `A005150 <http://oeis.org/A005150>`_ ，好像是没有通项公式的。
"""

from typing import *

import functools

class Solution:
    @functools.lru_cache()
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            previousTerm = self.countAndSay(n - 1)
            res = []
            lastCharacter = previousTerm[0]
            lastCharacterPosition = 0

            for i, v in enumerate(previousTerm[1: ] + "\x00", 1):
                if v != lastCharacter:
                    res.append(str(i - lastCharacterPosition) + lastCharacter)
                    lastCharacter = v
                    lastCharacterPosition = i
                else:
                    continue
            
            # print(res)
            return "".join(res)

# s = Solution()
# print(s.countAndSay(5)) # 111221
# print(s.countAndSay(30))