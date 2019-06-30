"""
解析布尔表达式。

这题我用了非常耍赖的做法，用了 ``eval`` ，因为我还没学编译原理……等我学了编译原理之后再来搞定这些parse类题目吧。
"""

from typing import *

from functools import reduce

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def And(*args):
            return reduce(lambda x, y: bool(x and y), args)
        
        def Or(*args):
            return reduce(lambda x, y: bool(x or y), args)

        def Not(arg):
            return bool(not arg)

        expression = expression.replace("t", "True").replace("f", "False").replace("&", "And").replace("|", "Or").replace("!", "Not") # 把所有t替换成True、f替换成False、&、|、!替换成刚才定义的函数

        return eval(expression) # eval就完事儿了

# s = Solution()
# print(s.parseBoolExpr(expression = "!(f)"))
# print(s.parseBoolExpr(expression = "|(&(t,f,t),!(t))"))