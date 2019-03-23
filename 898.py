"""
给一个array，对于其中的每个substring（连续的），都把自己的每个元素全部做一次按位或，问你这些substring总共能产生多少种结果。

文字描述挺麻烦的，用数学描述大概是这样

.. math::

    \{a_i | a_{i + 1} | ... | a_j: 0 \leq i \leq j \leq n - 1\}

问上面的这个集合里有多少个元素。

.. note:: :math:`O(n^2)` 是会超时的。


"""

from typing import *

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # if A:
        #     res = set()
            
        #     for i in range(len(A)):
        #         temp = A[i]

        #         for j in range(i, len(A)):
        #             temp = temp | A[j]
        #             res = res.union((temp, ))

        #     return len(res)
        # else:
        #     return 0
        # 一改：O(n^2)是会time limit exceed的。

        