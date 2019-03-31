r"""
把一个数写成 **-2进制** 。

比如

.. math::

    \begin{aligned}
        2 &= 1 \times (-2)^2 + 1 \times (-2)^1 + 0 \times (-2)^0 = (110)_{-2} \\
        3 &= 1 \times (-2)^2 + 1 \times (-2)^1 + 0 \times (-2)^1 = (111)_{-2} \\
        4 &= 1 \times (-2)^2 + 0 \times (-2)^1 + 0 \times (-2)^0 = (100)_{-2} \\
    \end{aligned}

还是用除法取余数的方法。被除数现在是-2，是一个负数，但是规则和被除数是正数的时候没什么区别，都是要找到

.. math::

    n = -2 \times d + r, \qquad r \in \{0, 1\}

中 :math:`d, r` 的整数解，其中注意 :math:`r` 只能取0或者1。这个规则也很简单，先看n是偶数还是奇数，如果n是偶数，那么 :math:`r` 一定是0；如果n是奇数， :math:`r` 一定是1，再算出 :math:`d` 就可以了。每次记录下 :math:`r` 的值，再把 :math:`n` 置为新的 :math:`d` ，继续迭代，直到 :math:`n = 0` 。最后的结果就是每次的 :math:`r` 的倒序。

以6为例

::
         d           r
    -2 | 6 --------- 0
    -2 | -3 -------- 1
    -2 | 2 --------- 0
    -2 | -1 -------- 1
    -2 | 1 --------- 1
    -2 | 0

这样结果是 :math:`6 = (11010)_{-2}` 。
"""

from typing import *

class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"

        res = []

        while N != 0:
            # if N > 0:
            #     remainder = N % 2
            #     N = - (N // 2)
            # elif N == -1:
            #     remainder = 1
            #     N = 1
            # # elif N == 1:
            # #     remainder = 1
            # #     N = 0
            # else:
            #     remainder = (- N) % 2
            #     N = (- N) // 2
            if N % 2 == 0: # N是偶数
                remainder = 0 # r一定是0
                N = - (N // 2) # 算出d，作为下一轮新的N
            else: # N是奇数
                remainder = 1 # r一定是1
                N = (N - 1) // -2 # 算出d，作为下一轮新的N
            res.append(str(remainder)) # 记录r

        return "".join(res[:: -1]) # 结果是r的倒序

# s = Solution()
# print(s.baseNeg2(2))
# print(s.baseNeg2(3))
# print(s.baseNeg2(4))
# print(s.baseNeg2(5))
# print(s.baseNeg2(6))