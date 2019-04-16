"""
解方程

我觉得这一题的难点在于，怎样在不使用 ``eval()`` 的前提下，把含有字母 ``x`` 的表达式解析出来，得到字母前的常系数和常数项。

我仍然采用的是非常传统的遍历、分段解析的方法，遇到加号或者减号，说明前面的加和项已经结束了，后面开始的是新的一个加和项，所以就把缓存区里的表达式先解析出来。
"""

from typing import *

class Solution:
    def solveEquation(self, equation: str) -> str:
        lhs, rhs = equation.split("=") # 分离出左边表达式和右边表达式
        lhsCoefficients = self.statementToCoefficients(lhs) # 把左边表达式的多项式系数解析出来
        rhsCoefficients = self.statementToCoefficients(rhs) # 把右边表达式的多项式系数解析出来
        if lhsCoefficients[0] == rhsCoefficients[0] and lhsCoefficients[1] != rhsCoefficients[1]: # 如果x前的系数相同、但是常数不同，那么是没有解的
            return "No solution"
        elif lhsCoefficients[0] == rhsCoefficients[0] and lhsCoefficients[1] == rhsCoefficients[1]: # 如果x前的系数相同、常数也相同，那么是有无限多个解的
            return "Infinite solutions"
        else: # 此外都是有唯一解的情况
            res = (rhsCoefficients[1] - lhsCoefficients[1]) // (lhsCoefficients[0] - rhsCoefficients[0])
            return f"x={res}"

    def statementToCoefficients(self, statement: str) -> tuple: # 把表达式解析成x^1, x^0前的系数
        res = [0, 0]
        buffer = ""

        for i, v in enumerate(statement + "+0"): # 后面填个 +0 省得最后出for之后再解析
            if v == "+" or v == "-": # 遇到了加号或者减号，说明buffer里的加和项已经结束了
                if "x" in buffer: # 看buffer里有没有字母，如果有字母，要把字母前面的系数解析出来
                    prefix = buffer[: buffer.index("x")] # 字母前面的系数
                    if prefix == "+" or prefix == "": # 有可能字母前面是空的或者只有一个加号
                        res[0] += 1
                    elif prefix == "-": # 有可能字母前面只有一个减号
                        res[0] -= 1
                    else: # 前面是一个有效的数字
                        res[0] += int(prefix)
                else: # 如果没有字母，说明是常数项
                    if buffer:
                        res[1] += int(buffer)
                buffer = v
            else:
                buffer = buffer + v

        return res

# s = Solution()
# assert s.solveEquation("x+5-3+x=6+x-2") == "x=2"
# assert s.solveEquation("x=x") == "Infinite solutions"
# assert s.solveEquation("2x=x") == "x=0"
# assert s.solveEquation("2x+3x-6x=x+2") == "x=-1"
# assert s.solveEquation("x=x+2") == "No solution"