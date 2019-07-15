"""
构造一个含有A个 ``a`` 和B个 ``b`` 的字符串，但是字符串里不能含有 ``aaa, bbb`` 。

肯定是在满足条件的情况下，尽量保证 ``a, b`` 的可用库存平衡，如果出现不平衡，比如 ``a`` 的可用库存比 ``b`` 大，就尽量多追加 ``a`` 。在实在没有办法的时候，比如前两个字符都是 ``a`` 、再追加 ``a`` 就会违反规则的时候，再追加 ``b`` 。

这个应该就是是所谓的greedy吧。
"""

from typing import *

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res = ["\x00", "\x00"] # 前面先填两个dummy char省得判断越界

        while A > 0 or B > 0: # a和b都必须要有可用库存
            if res[-1] == "a" and res[-2] == "a": # 最后两个字符都是a
                res.append("b") # 别无选择，只能追加b
                B -= 1
            elif res[-1] == "b" and res[-2] == "b": # 最后两个字符都是b
                res.append("a") # 别无选择，只能追加a
                A -= 1
            else: # 不然的话就尽可能保持a和b的库存平衡
                if A > B: # 如果a的库存比b大
                    res.append("a") # 尽量追加a
                    A -= 1
                else: # b的库存比a大
                    res.append("b") # 尽量追加b
                    B -= 1

        return "".join(res[2: ])

# s = Solution()
# print(s.strWithout3a3b(1, 2))
# print(s.strWithout3a3b(4, 1))