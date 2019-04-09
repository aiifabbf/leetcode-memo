"""
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