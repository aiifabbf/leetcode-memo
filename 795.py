r"""
一个array的所有满足最大值在 ``[L, R]`` 区间里的substring（要连续）有多少个？

即求集合

.. math::

    \{(i, j) | \max\{a_i, a_{i + 1}, ... a_j}\} \in [L, R], 0 \leq i \leq j \leq n - 1\}

的大小。

试着用动态规划做。设 :math:`p_i` 是以第i个元素为结尾的所有满足条件的substring的个数。那么 :math:`p_i` 和前面的项有什么关系？

-   如果 :math:`a_i > R` ，那么 :math:`p_i = 0`

    因为无论 :math:`a_i` 和前面的元素怎么组合，最大值都肯定不会小于 :math:`a_i` ，所以直接就是0个。

-   如果 :math:`L \leq a_i \leq R` ，那么一路往前，直到遇到第一个大于R的数 :math:`a_j` ，这之间的数 :math:`[j + 1, i]` 一共 :math:`i - j` 个，都可以组合，所以 :math:`p_i = i - j` ；如果一路往前都没有遇到任何一个大于R的数，说明 :math:`[0, i]` 之间一共 :math:`i + 1` 个数都可以组合，所以 :math:`p_i = i + 1`
-   如果 :math:`a_i < L` ，那么只有自己肯定是不行的，必须一路往前，找到第一个在范围 :math:`[L, R]` 内的数 :math:`a_j` 才能开始组合，这时候 :math:`p_i = p_j` ；一旦在遇到 :math:`a_j` 之前，遇到了一个大于R的数，那么只能作废，这时候 :math:`p_i = 0` 。

可以给上面的动态规划过程做一点优化

-   :math:`a_i < L` 的情况，其实一个 :math:`p_i = p_{i - 1}` 就可以了，不需要那么麻烦还要往前找。因为 :math:`a_i < L` 一定能够保证当 :math:`a_i` 追加到以 :math:`a_{i - 1}` 结尾的所有满足条件的substring时，这些substring的最大值不会有变化，所以随便加。
-   :math:`L \leq a_i \leq R` 的情况也可以优化，可以用一个数记录一下最近遇到的大于R的数的下标，这样就不用每次去从后往前找了。
-   当然还有老生常谈的，一边DP一边加，省得最后再加。
-   最后，既然不用往前找了，那么就会发现每次只会用到 :math:`p_{i - 1}` ，所以之前的也就没必要存着了。 ``dp`` 就可以从array变成一个数了。
"""

from typing import *

class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        if L <= A[0] <= R:
            # dp = [1]
            dp = 1
            summation = 1
            lastAboveBoundElementPosition = -1 # 用一个数记录一下最近遇到的大于R的数的下标
        else:
            # dp = [0]
            dp = 0
            summation = 0
            if A[0] > R:
                lastAboveBoundElementPosition = 0
            else:
                lastAboveBoundElementPosition = -1

        for i, v in enumerate(A[1: ], 1):
            if v > R: # 如果a_i > R，那么绝对没机会
                # dp.append(0)
                dp = 0
                lastAboveBoundElementPosition = i
            elif L <= v <= R: # 如果L <= a_i <= R，那么往前找，直到遇到一个a_j > R

                # for j in reversed(range(0, i)): # 往前找一个a_j > R
                #     if A[j] > R: # 遇到了a_j
                #         dp.append(i - j) # [j + 1, i]之间的数，一共i - j个数，都可以组合
                #         break
                #     else:
                #         continue
                # else: # a_i前面的数都小于等于R，那么[0, i]之间的数，一共i + 1个数全部都可以组合
                #     dp.append(i + 1)

                # if lastAboveBoundElementPosition == -1:
                #     # dp.append(i + 1)
                #     dp = i + 1
                #     summation += i + 1
                # else:
                #     # dp.append(i - lastAboveBoundElementPosition)
                #     dp = i - lastAboveBoundElementPosition
                #     summation += i - lastAboveBoundElementPosition
                # 这两种情况可以合并，省一个判断
                dp = i - lastAboveBoundElementPosition
                summation += dp

            else: # v < L

                # for j in reversed(range(0, i)): # 往前找一个L <= a_j <= R
                #     if A[j] > R: # 一旦遇到了一个大于R的数
                #         dp.append(0) # 全部作废
                #         break
                #     elif L <= A[j] <= R: # 遇到了范围内的数a_j
                #         dp.append(dp[j]) # p_i = p_j
                #         break
                #     else: # 遇到了小于L的数
                #         continue # 没关系，继续往前找
                # else: # 找了一圈都没有找到范围内的数，也没有大于R的数，说明前面的数全部都是小于L的数
                #     dp.append(0) # 那么也没有办法组合，只能是0
                
                # dp.append(dp[-1]) # 其实这种情况下，一个p_i = p_{i - 1}就解决了，因为a_i小于L，所以加到以a_{i - 1}结尾的substring里，肯定不影响这些substring的最大值
                summation += dp

        return summation

# s = Solution()
# assert s.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3) == 3
# assert s.numSubarrayBoundedMax([73,55,36,5,55,14,9,7,72,52], 32, 69) == 22
# assert s.numSubarrayBoundedMax([34,46,51,92,50,61,49,82,4,4], 18, 84) == 24
# assert s.numSubarrayBoundedMax([876,880,482,260,132,421,732,703,795,420,871,445,400,291,358,589,617,202,755,810,227,813,549,791,418,528,835,401,526,584,873,662,13,314,988,101,299,816,833,224,160,852,179,769,646,558,661,808,651,982,878,918,406,551,467,87,139,387,16,531,307,389,939,551,613,36,528,460,404,314,66,111,458,531,944,461,951,419,82,896,467,353,704,905,705,760,61,422,395,298,127,516,153,299,801,341,668,598,98,241], 658, 719) == 19