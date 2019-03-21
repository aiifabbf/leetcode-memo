"""
判断是否存在一个 :math:`i, 0 < i < n - 1` 使得长度为n - 1的array满足

.. math::

    \left\{\begin{aligned}
        a_0 < a_1 < ... < a_i \\
        a_i > a_{i + 1} > ... > a_{n - 1} \\
    \end{aligned}\right.

直观上来说就是判断一个array里面的值从左往右是否形成了一个峰。
"""

from typing import *

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return False
        else:
            peekMet = False

            for i, v in enumerate(A[1: -1], 1):
                if A[i - 1] < v < A[i + 1]:
                    if peekMet:
                        return False
                elif A[i - 1] < v > A[i + 1]:
                    if peekMet:
                        return False
                    else:
                        peekMet = True
                elif A[i - 1] > v > A[i + 1]:
                    if not peekMet:
                        return False
                else:
                    return False
            else:
                if peekMet:
                    return True
                else:
                    return False