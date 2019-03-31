"""
把一个数组分成两个非空subsequence（不一定要连续），使得两个subsequence的平均值相等。如果可以做到，就返回true，也有可能做不到，那就返回false。

难点在于是subsequence而不是substring，如果是substring就很好办……

有一个定理是，如果这个array里存在一个subsequence使得这个subsequence的平均值和剩下的所有的值的平均值相等，那么这个subsequence的平均值一定就是整个array的平均值。

.. note::

    可以简单证明一下，假设array是 :math:`\{a_1, a_2, ..., a_n\}` ，经过重排之后，array变成 :math:`\{a'_1, a'_2, ..., a'_n\}` ，其中前 :math:`j` 个元素就是这个满足条件的subsequence。因此有

    .. math::

        {\sum_{i = 1}^n a'_i \over n} = {\sum_{i = 1}^j a'_i \over j}

    变换过程如下

    .. math::

        \begin{aligned}
            j \sum_{i = 1}^n a'_i &= n \underbrace{\sum_{i = 1}^j a'_i}^{subsequence之和} \\
            j \sum_{i = 1}^n a'_i &= n \underbrace{\left(\sum_{i = 1}^n a'_i - \sum_{i = j + 1}^n a'_i\right)}_{等于array之和减去剩下元素的和} \\
            (n - j) \sum_{i = 1}^n a'_i &= n \underbrace{\sum_{i = j + 1}^n a'_i}_{剩下元素之和} \\
            {\sum_{i = 1}^n a'_i \over n} &= \underbrace{\sum_{i = j + 1}^n a'_i \over n - j}_{剩下元素的平均值}
        \end{aligned}

    由此得到

    .. math::

        {\sum_{i = 1}^n a'_i \over n} = {\sum_{i = 1}^j a'_i \over j} = \sum_{i = j + 1}^n a'_i \over n - j}


"""

from typing import *

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        

# s = Solution()
# assert s.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8])