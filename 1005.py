"""
从array里选一个数，把这个数变成自己的倒数，这样的操作做k次，问操作结束后array和的最大值是多少。

首先肯定是想办法把array里面的负数先倒一倒，全部变成正数。这里会出现两种情况

-   k小于array里负数的个数

    所以做不到把array里每个负数都变成正数，这时候就要选择一些负数、把它们变成正数，显然应该取最小的那些负数，这样倒过来之后会变成很大的正数。

-   k等于array里负数的个数

    一切OK，不多不少，所有负数都变成正数。

-   k大于array里负数的个数

    这时候可以用掉一点k，先把array里所有的负数都变成正数。做完这个之后，剩下的次数有两种情况

    -   是偶数

        那么可以随便选一个数来来回回倒来倒去，最后反正和也不变。

    -   是奇数

        最后总会剩下一次，所以要选array里最小的数颠倒成负数。
"""

from typing import *

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        array = sorted(A)
        numberOfNegativeNumbers = len([True for v in array if v < 0]) # array里负数的个数
        if numberOfNegativeNumbers >= K: # k小于等于负数的个数

            for i in range(K): # 把最小的k个负数变成倒数
                array[i] = -array[i]

            return sum(array)
        else: # k大于负数的个数
            if (K - numberOfNegativeNumbers) % 2 == 0: # 把所有负数都变成正数之后，剩余的次数是偶数
                return sum(abs(v) for v in array) # 无事发送
            else: # 剩余的次数是奇数
                array = [abs(v) for v in array]
                return sum(array) - min(array) * 2 # 选最小的那个数颠倒成负数

# s = Solution()
# print(s.largestSumAfterKNegations([4, 2, 3], 1)) # 5
# print(s.largestSumAfterKNegations([3, -1, 0, 2], 3)) # 6
# print(s.largestSumAfterKNegations([2, -3, -1, 5, -4], 2)) # 13
# print(s.largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6)) # 22