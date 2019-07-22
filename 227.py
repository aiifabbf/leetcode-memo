"""
实现一个支持自然数、加减乘除的计算器，不用管括号，但要关注乘除的优先级。

Tokenize步骤和 `224 <./224.py>`_ 一样。然后我以为这道题总归该用到AST了吧……但是其实还是用stack就可以搞定了。因为乘除号的优先级高于加减号，所以把evaluate分成两个阶段

1.  处理掉所有乘除号，使得剩下的token list里只含有数字和加减号
2.  处理只含有加减号的token list

我猜 `Basic Calculator III <https://leetcode.com/problems/basic-calculator-iii/>`_ 应该是实现一个支持自然数、加减乘除、括号的完整计算器吧，可惜这题居然要氪金，差评。
"""

from typing import *

import re
import collections
import itertools
import functools

class Solution:
    def calculate(self, s: str) -> int:
        patternString = "".join([
            r"(0|[1-9][0-9]*)", # 自然数
            r"|",
            r"([+]|-|[*]|/)", # 加减乘除
        ])
        pattern = re.compile(patternString)
        tokens = (v.group() for v in pattern.finditer(s))
        return self.evaluateTokens(tokens)

    def evaluateTokens(self, tokens: "Iterable") -> int:
        stack = collections.deque()
        buffer = collections.deque()

        while True:
            if buffer:
                token = buffer.popleft()
            else:
                token = next(tokens, None)
                if token == None:
                    break
            v = token
            if v.lstrip("+-").isdigit(): # 数字
                if stack and (stack[len(stack) - 1] == "*" or stack[len(stack) - 1] == "/"): # stack非空并且顶端是乘除号
                    operator = stack.pop()
                    thatNumber = stack.pop()
                    if operator == "*":
                        buffer.appendleft(str(int(thatNumber) * int(v))) # evaluate a*b
                    else:
                        buffer.appendleft(str(int(thatNumber) // int(v))) # evaluate a/b
                else: # stack空、或者非空但是顶端是加减号
                    stack.append(token) # 不处理，直接push
            else: # 加减乘除号
                stack.append(token) # 直接push
        # 这个phase结束之后，stack上只有数字、加减号了

        if stack:
            return self.evaluatePlusMinusTokens(stack) # phase 2只处理加减号
        else:
            return 0

    def evaluatePlusMinusTokens(self, tokens: "Iterable") -> int:
        # stack = collections.deque()

        # for token in tokens:
        #     v = token
        #     if v.lstrip("+-").isdigit():
        #         if stack:
        #             operator = stack.pop()
        #             thatNumber = stack.pop()
        #             if operator == "+":
        #                 stack.appendleft(str(int(thatNumber) + int(v)))
        #             else:
        #                 stack.appendleft(str(int(thatNumber) - int(v)))
        #         else:
        #             stack.append(token)
        #     else:
        #         stack.append(token)

        # if stack:
        #     return int(stack[0])
        # else:
        #     return 0
        # 只处理加减的时候其实没必要用stack了

        # iterator = iter(tokens)
        # res = next(iterator, None)
        # if res == None:
        #     return 0
        # else:
        #     res = int(res)

        #     while True: # 每次从token list里取两个元素
        #         operator = next(iterator, None) # 第一个是加减号
        #         if operator == None: # 发现token list空了
        #             return res
        #         thatNumber = next(iterator) # 第二个是加数或者减数
        #         if operator == "+":
        #             res = res + int(thatNumber)
        #         else:
        #             res = res - int(thatNumber)
        # 这不是典型的reduce吗

        return functools.reduce(lambda v, w: v + int(w), map(lambda v: v[0] + v[1], zip(itertools.islice(tokens, 1, None, 2), itertools.islice(tokens, 2, None, 2))), int(tokens[0])) # 速度和上面的做法差不多，但是可读性差多了（装逼性好多了）

# s = Solution()
# print(s.calculate("3")) # 3
# print(s.calculate("3+2*2")) # 7
# print(s.calculate(" 3/2 ")) # 1
# print(s.calculate(" 3+5 / 2")) # 5