"""
把一个数n全部用完全平方数 ``1, 4, 9, ...`` 的和表示，最少需要多少个完全平方数？可以重复使用完全平方数。

我一开始以为是贪心，直接找小于等于n的最大的完全平方数，然后递归，但是 ``12`` 是一个特例，最佳组合不是 ``9 + 1 + 1 + 1`` 而是 ``4 + 4 + 4`` 。

有一个拉格朗日四平方数定理 [#]_ 是说，任何一个正整数都可以用最多4个完全平方数的和表示。所以结果只可能是 ``1, 2, 3, 4`` 中的一个

-   如果n自己就是完全平方数，那么结果是1
-   如果n能写成 :math:`4 ^ a (8b + 7)` 的形式，那么结果是4

    这是勒让德三平方数定理的推论 [#]_ 。
    
    其实勒让德三平方数定理的内容是，如果n不能写成 :math:`4 ^ a (8b + 7)` 的形式，那么最多可以写成三个数的平方和，意思是可以写成1个或者2个或者3个数的平方和，但不用写成4个数的平方和。所以反过来就是如果不能写成这个形式，结果一定是4。

-   如果n能写成2个完全平方数的和，那么n减去一个完全平方数剩下的部分还是一个完全平方数

    这好像是废话。

.. [#] https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
.. [#] https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
"""

from typing import *

import math

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        largestSquareLessOrEqualThanN = math.floor(math.sqrt(n))
        if n == largestSquareLessOrEqualThanN ** 2: # 如果n自己就是平方数
            return 1 # 那么用自己就可以表示自己，所以结果是1
        else: # n不是平方数
            temp = n # 用勒让德三平方数定理看结果是不是4

            while temp % 4 == 0:
                temp = temp >> 2 # 不停地整除4，消去 4^a
            
            if temp % 8 == 7: # 检验剩下的8b + 7部分
                return 4
            else:

                for i in range(1, math.ceil(math.sqrt(n))): # 只要从1试到floor(sqrt(n))就可以了
                    if self.isSquareNumber(n - i ** 2): # 剩下的部分仍然是完全平方数
                        return 2
                else:
                    return 3

    def isSquareNumber(self, n):
        largestSquareLessOrEqualThanN = math.floor(math.sqrt(n))
        if n == largestSquareLessOrEqualThanN ** 2:
            return True
        else:
            return False

# s = Solution()
# assert s.numSquares(12) == 3
# assert s.numSquares(13) == 2
# assert s.numSquares(8285) == 2
# assert s.numSquares(192) == 3
# assert s.numSquares(18) == 2