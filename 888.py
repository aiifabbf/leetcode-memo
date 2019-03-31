r"""
交换两个array的元素一次，使两个array各自的累加和相等。也就是array A选一个元素给array B、array B也选一个元素给array A。

暴力做法就是遍历A里的每个元素 :math:`a_i` ，每次遍历再遍历B里的每个元素 :math:`b_j` ，一旦发现有 :math:`\summation_{k = 0}^m a_k - a_i + b_j = \summation_{k = 0}^n b_k - b_j + a_i` 的，就返回这一对 ``[ai, bj]`` 。复杂度是 :math:`O(mn)` 。会超时。

因为判断一个元素是否在一个集合里的复杂度是 :math:`O(1)` ，所以我想到了这种做法：遍历A中的每个元素 :math:`a_i` ，此时如果B中存在能够交换出来的元素 :math:`b_j` ，那么 :math:`b_j` 应该满足

.. math::

    b_j = {\summation_{k = 0}^n - \summation_{k = 0}^m + 2 a_i over 2}

所以每次遍历到一个 :math:`a_i` ，都来判断一下 :math:`{\summation_{k = 0}^n - \summation_{k = 0}^m + 2 a_i over 2}` 在不在array B里面。但是如果直接判断在不在array B，判断一次的复杂度是 :math:`O(n)` ，还是很慢，所以就事先把array B变成set B，这样每次判断复杂度变成了 :math:`O(1)` 就很快了。
"""

from typing import *

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        # summationA = sum(A)
        # summationB = sum(B)

        # for v1 in A:
            
        #     for v2 in B:
        #         if summationA - v1 + v2 == summationB - v2 + v1:
        #             return [v1, v2]
        # O(mn)貌似不大行

        summationA = sum(A)
        summationB = sum(B)
        delta = summationB - summationA
        setB = set(B)

        for v in A:
            target = (delta + 2 * v) // 2 # 如果存在，array B应该拿出的元素应该是这个大小
            if target in setB: # 判断一个元素在不在set里是O(1)
                return [v, target]

# s = Solution()
# print(s.fairCandySwap([1, 1,], [2, 2]))
# print(s.fairCandySwap([1, 2,], [2, 3]))