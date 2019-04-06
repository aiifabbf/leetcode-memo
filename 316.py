"""
删掉一个字符串里所有的重复字符，使每个字符只出现一次。但是删不是乱删，要删的恰到好处，使整个字符串的字典排序值 [#]_ 最小。

.. [#] 字典排序在 https://en.wikipedia.org/wiki/Lexicographical_order 这里有介绍。
"""

from typing import *

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()

        for v in s:
            if v in seen:
                index = stack.index(v)
                deletedAndAppended = stack[: index] + stack[index + 1: ]
                if deletedAndAppended < stack:
                    stack = deletedAndAppended
                else:
                    pass
            else:
                stack.append(v)
                seen.add(v)
            
        return "".join(stack)

s = Solution()
print(s.removeDuplicateLetters("bcabc"))
print(s.removeDuplicateLetters("cbacdcbc"))