"""
写一个支持括号、加号、减号、正数的计算器

好像又是编译原理……
"""

from typing import *

import string
import collections
import re
import queue

class Solution:
    def calculate(self, s: str) -> int:
        categories = collections.defaultdict(lambda: "Number")
        # categories.update({v: "Number" for v in string.digits})
        categories.update({
            "+": "Operator",
            "-": "Operator",
        })
        categories.update({
            "(": "LeftParenthese",
            ")": "RightParenthese",
        })
        # tokens = list(map(lambda v: "".join(v[1]), itertools.groupby(s.replace(" ", ""), key=categories.__getitem__)))
        # 用itertools.groupby()不行，因为会把 `))` 黏在一起

        # tokens = [("\x00", "undefined")]

        # for v in s:
        #     if categories[v] == "Number" and categories[tokens[-1][0]] == "Number":
        #         tokens[-1] = (tokens[-1][0] + v, tokens[-1][1])
        #     elif v != " ":
        #         tokens.append((v, categories[v]))

        # tokens = tokens[1: ]
        # 可以完全自己实现tokenizer

        patternString = r"(0|[1-9][0-9]*)" \
            r"|(\+|-)" \
            r"|(\(|\))"
        pattern = re.compile(patternString)
        tokens = queue.deque([(v.group(), categories[v.group()]) for v in pattern.finditer(s)])
        # 直接用re也不错

        # print(tokens)

        return self.evaluateTokens(tokens)

    def evaluateTokens(self, tokens: List) -> int:
        if not tokens:
            return 0
        elif len(tokens) == 1:
            return int(tokens[0][0])

        stack = queue.deque()

        while tokens:
            token = tokens.popleft()
            v, category = token
            if category == "LeftParenthese":
                stack.append(token)
            elif category == "RightParenthese":
                tokens.insert(0, stack.pop())
                stack.pop()
            elif category == "Number":
                if stack and stack[len(stack) - 1][1] == "Operator":
                    op = stack.pop()[0]
                    thatNumber = stack.pop()[0]
                    if op == "+":
                        tokens.insert(0, (str(int(v) + int(thatNumber)), "Number"))
                    else:
                        tokens.insert(0, (str(int(thatNumber) - int(v)), "Number"))
                else:
                    stack.append(token)
            else:
                stack.append(token)

        return self.evaluateTokens(stack)

s = Solution()
print(s.calculate("")) # 0
print(s.calculate("1")) # 1
print(s.calculate("1 + 1")) # 2
print(s.calculate(" 2-1 + 2")) # 3
print(s.calculate("0-1")) # -1
print(s.calculate("0-1+2")) # 1
print(s.calculate("(1+(4+5+2)-3)+(6+8)")) # 23
print(s.calculate("8+4-(1)")) # 11
print(s.calculate("8+4-(1)+8-10")) # 9
print(s.calculate("2-4-(8+2-6+(8+4-(1)+8-10))")) # -15
print(s.calculate("1+7-7+3+3+6-3+1-8-2-6-1+8-0+0-2+0+10-6-9-9+0+6+4+2+7+1-4-6-6-0+6+3-7+0-4+10-2-5+6-1-3+7+7+2+0+2-8+7+2-3-8-9-6+10-7-6+3-8+5+6-7-10-6-8-10-8+1+9+1-9-1+10+10+3+7-1-10+1-0-7+0-3-3+4+7-9-10-1+4-8-3-0-1-0-3+5-10+6-6-0-6-6-7+7+10+10-5-9-10-2-8+9-2-8-7-9-0-6-5-1+1+3+8-5-8+3-9+9+6-5+0-2+0+8+8-4+6+1-2-0-10-8+1-2-8+2-2-2-4+2+5+3-9+1+9-8+9-8+7+10+1+10-9+2+2+8+7-10-8+6+6+3+0+4-1+0+7-3+8-8-4+8-6-6+3-3-9+6+4+6+7-2-0+6-10+8-2-4+3-8+1-2+8+1-2-4-3-9-4-1-3+5+9+7-8-2+7-10+7+9+1+5-5+8-3-10-7-1-7+10+3+2-8-8+0+9+3+6+8+4+2+10+8+6-1+2+10-5+5+4-2+10+7-6-5+9-9+5-5-2+5+2-1+7-8+4-2+2+2+5-10-7-0+5-8-6-10-5+9-1+1-8+10-7+2-3-3+2+3-8+4-6-7+3-0+6-6-3+1+2-6+2+3+0-4-0+3-5-1-4-0+9+5-6+3-10+0+10-4+6-6-5-6+5+3+7-4+6+2+0+10+4-3+10-10-0-10-4-8+9-5-0-0-9-8-3-2+6"))
with open("/home/benjamin/a.test") as f:
    print(s.calculate(f.read()))