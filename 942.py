"""
给一个只含 ``I`` 和 ``D`` 的长度为n的字符串 :math:`\{s_i\}`，输出一种 :math:`[0, 1, 2, ..., n]`` 的排列方式 :math:`\{a_i\}` 使得

.. math::

    \left\{\begin{aligned}
        && a_i < a_{i + 1}, \qquad s_i = I \\
        && a_i > a_{i + 1}, \qquad s_i = D
    \end{aligned}\right.

简单来说就是遇到一个 ``I`` ，就要求排列里同一个位置的数字要严格递增；遇到一个 ``D`` ，就要求排列里同一个位置的数字要严格递减。

思路是先不要管排列方式一定要在那个范围里面，先直接从0开始，遇到一个 ``I`` 就把至今为止用到过的最大数加上一放进去；同理遇到一个 ``D`` 就把至今位置用到过的最小的数减一放进去。然后再整个array每个元素都加上最小的数的负数，相当于把整个array向上平移几个单位，就能把整个array放入 :math:`[0, 1, 2, ..., n]`` 的范围里面。
"""

from typing import *

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        pool = [0] # 从0开始
        maximum = 0
        minimum = 0

        for v in S:
            if v == "I": # 遇到一个I
                pool.append(maximum + 1) # 把至今为止用过的最大的数加一放进去
                maximum += 1 # 更新至今为止用过的最大的数
            elif v == "D": # 遇到一个D
                pool.append(minimum - 1) # 把至今位置用过的最小的数减一放进去
                minimum -= 1 # 更新至今位置用过的最小的数

        return [i - minimum for i in pool] # 这样最小的数是minimum，要把整个array平移到0以上，只要每个数都加上- minimum就可以了。