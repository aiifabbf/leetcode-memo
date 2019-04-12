"""
去除外层括号

就是每匹配到一个 ``(A)`` ，其中 ``A`` 可以是任何东西，可以是空字符串、可以是括号组，都把外面的括号去掉。
"""

from typing import *

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        primitives = []
        buffer = ""

        for i, v in enumerate(S):
            if v == "(":
                stack.append(v)
                buffer += v
            else:
                buffer += v
                stack.pop()
                if stack == []:
                    # print(buffer)
                    primitives.append(buffer[1: -1])
                    buffer = ""
                else:
                    pass

        # print(primitives)
        return "".join(primitives)

# s = Solution()
# print(s.removeOuterParentheses("(()())(())"))
# print(s.removeOuterParentheses("(()())(())(()(()))"))
# print(s.removeOuterParentheses("()()"))