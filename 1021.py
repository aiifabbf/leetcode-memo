"""
找到

.. math::

    \max\{a_i + a_j + i - j | 0 \leq i < j \leq n - 1}

最差 :math:`O(n^2)` ，想找一个 :math:`O(n)` 的解决方法。
"""

from typing import *

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # i = 0
        # j = 1
        # maximum = A[i] + A[j] + i - j

        # while i + 1 < j < len(A) - 1:
        #     print(i, j)
        #     moveLeftTarget = A[i + 1] + A[j] + i + 1 - j
        #     moveRightTarget = A[i] + A[j + 1] + i - (j + 1)
        #     moveWholeRightTarget = A[i + 1] + A[j + 1] + i - j
        #     if moveLeftTarget == max(moveLeftTarget, moveRightTarget, moveWholeRightTarget):
        #         i += 1
        #         maximum = max(maximum, moveLeftTarget)
        #         continue
        #     elif moveRightTarget == max(moveLeftTarget, moveRightTarget, moveWholeRightTarget):
        #         j += 1
        #         maximum = max(maximum, moveRightTarget)
        #         continue
        #     else:
        #         i += 1
        #         j += 1
        #         maximum = max(maximum, moveWholeRightTarget)
        #         continue
        
        # return maximum

        # maximum = float("-inf")

        # for i in range(len(A) - 1):
            
        #     for j in range(i + 1, len(A)):
        #         maximum = max(maximum, A[i] + A[j] + i - j)

        # return maximum
        # 有人说暴力是可以过的，我信了。

# s = Solution()
# assert s.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
# assert s.maxScoreSightseeingPair([3, 7, 2, 3]) == 9
# assert s.maxScoreSightseeingPair([2,7,5,8,8,8]) == 15