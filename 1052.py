r"""
有两个向量A、B，B中每一维都是0或者1，可以选择把B中某一维开始的之后的连续相邻的k维上的数字全部变成0，问

.. math::

    A^T \dot (1 - B)

的最大值是多少。

假设两个向量的维数是n，那么这道题就相当于是一个( :math:`(n - k) \times n` )乘一个n维的向量，需要做 :math:`(n - k) \times n` 次乘法，所以复杂度是 :math:`O(n ^ 2)` 。

但其实其中有相当多次的乘法是重复计算的，可以想办法省下来，使得复杂度可以降低到 :math:`O(n)` 。做法就是非常简单的差量更新，维护一个窗口，窗口移动到下一个格子的时候，假设窗口的第一个格子是第i个格子，那么就减去第i-1个格子的、加上第i-1+k个格子的值。
"""

from typing import *

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        dotProduct = sum(customers[j] * (- grumpy[j] + 1) for j in range(len(grumpy))) # 不改变B向量里任何一维的值
        delta = sum(customers[j] for j in range(0, X)) - sum(customers[j] * (- grumpy[j] + 1) for j in range(0, X)) # 如果把[0, X)维上的值全部变成1，需要加上的量
        res = dotProduct + delta

        for i in range(1, len(grumpy) - X + 1):
            delta = delta - customers[i - 1] + customers[i - 1 + X] + customers[i - 1] * (- grumpy[i - 1] + 1) - customers[i - 1 + X] * (- grumpy[i - 1 + X] + 1)  # 如果把[i, i+X)维上的值全部变成1，需要加上的量
            res = max(res, dotProduct + delta)

        return res

# s = Solution()
# print(s.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3)) # 16
# print(s.maxSatisfied([1], [0], 1)) # 1
# print(s.maxSatisfied([10, 1, 7], [0, 0, 0], 2)) # 18
# print(s.maxSatisfied([2,6,6,9], [0,0,1,1], 1)) # 17