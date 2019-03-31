"""
给一个array，对于其中的每个substring（连续的），都把自己的每个元素全部做一次按位或，问你这些substring总共能产生多少种结果。

文字描述挺麻烦的，用数学描述大概是这样

.. math::

    \{a_i | a_{i + 1} | ... | a_j: 0 \leq i \leq j \leq n - 1\}

问上面的这个集合里有多少个元素。

.. note:: 暴力搜索 :math:`O(n^2)` 是会超时的。

还是用动态规划，想办法把前面计算过的结果缓存起来给下一次用。

设array :math:`P_i` 是以第i个元素为最后一个元素的所有substring的按位或的所有结果。那么 :math:`P_i` 和前面的项有什么关系呢？很容易发现， :math:`P_i` 里面的每一项，都是 :math:`P_{i - 1}` 里面的每一项和 :math:`a_i` 按位或的结果、还有 :math:`a_i` 本身，即

.. math::

    P_i = \{a_i \operatorname{or} v | v \in P_{i - 1}\} \cup \{a_i}

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

        res = {A[0], } # 全局结果
        tempSet = {A[0], } # 以第i个元素为结尾的所有substring的按位或的结果

        for i, v in enumerate(A[1: ], 1):
            tempSet = {v | value for value in tempSet}
            tempSet |= {v, } # P_i = \{a_i \operatorname{v} | v \in P_{i - 1}\} \cup \{a_i\}
            res |= tempSet # 一边更新全局结果，省得最后再reduce一次，节省一次遍历
            # print(tempSet, res)

        return len(res)

# s = Solution()
# print(s.subarrayBitwiseORs([1, 1, 2]))
# print(s.subarrayBitwiseORs([0]))
# print(s.subarrayBitwiseORs([1, 2, 4]))