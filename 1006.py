r"""
给一个数，在 ``N, N - 1, N - 2, ..., 3, 2, 1`` 这些数之间循环填充 ``*, //, +, -`` 号，问最后结果是多少。

最简单的做法是4个数4个数一读，然后算整个块的结果，加到结果里去，最后再根据剩下的数是4个还是3个还是2个还是1个，算出最后一个块的结果。

从这个题我发现了一个巨坑，就是涉及到整除符号的时候，一定一定要多加小心

.. code:: python3

    -6 * 5 // 4 + 3 == -5
    0 - 6 * 5 // 4 + 3 == -4

原因是

-   第一行的第一个减号是 **一元减号** ，优先级比乘、除、整除都要高，所以第一行的运算的过程实际上是 ``-6 * 5 // 4 + 3 == (-30) // 4 + 3 == (-8) + 3 == -5``
-   第二行 ``0`` 后面的减号是 **二元减号** ，优先级和普通的加减运算符一样，所以第二行的运算过程实际上是 ``0 - 6 * 5 // 4 + 3 == 0 - 30 // 4 + 3 == 0 - 7 + 3 == -4``
"""

from typing import *

class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 6
        elif N == 4:
            return 7
        else:
            buffer = []
            res = N * (N - 1) // (N - 2) + (N - 3) # 第一块的结果，前面没有减号，所以不太一样

            for i in reversed(range(1, N - 4 + 1)):
                # print(buffer)
                if len(buffer) < 4:
                    buffer.append(i)
                else:
                    res = res - (buffer[0] * buffer[1] // buffer[2]) + buffer[3]
                    buffer = [i]

            if buffer:
                if len(buffer) == 4:
                    res = res - (buffer[0] * buffer[1] // buffer[2]) + buffer[3]
                elif len(buffer) == 3:
                    res = res - (buffer[0] * buffer[1] // buffer[2])
                elif len(buffer) == 2:
                    res = res - buffer[0] * buffer[1]
                else:
                    res = res - buffer[0]
            
            return res

# s = Solution()
# assert s.clumsy(4) == 7
# assert s.clumsy(1) == 1
# assert s.clumsy(2) == 2
# assert s.clumsy(3) == 6
# assert s.clumsy(10) == 12