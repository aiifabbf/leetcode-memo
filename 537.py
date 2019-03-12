# 算复数

from typing import *

from functools import reduce
import operator
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        # a = complex(a.replace("i", "j"))
        # b = complex(b.replace("i", "j"))
        # 一改：输入可能会是 1+-i 这种狗屎形式

        # a = complex(*a.replace("i", "j").split("+"))
        # b = complex(*b.replace("i", "j").split("+"))
        a = reduce(operator.add, map(complex, a.replace("i", "j").split("+")))
        b = reduce(operator.add, map(complex, b.replace("i", "j").split("+")))

        q = a * b
        return f"{int(q.real)}+{int(q.imag)}i"

s = Solution()
assert s.complexNumberMultiply("1+1i", "1+1i") == "0+2i"
assert s.complexNumberMultiply("1+-1i", "1+-1i") == "0+-2i"