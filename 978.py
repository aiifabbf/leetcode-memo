"""
找到一个array的最长turbulent substring（要连续）

turbulent的意思是，这个array是锯齿状的。比如 ``[1, 2, 1, 3, 2]`` 这种array，一会后面的元素比前面大，紧接着又出现后面的元素比前一个小这种情况。

挺典型的动态规划题。设状态转移变量是 :math:`p_i` ，表示以第i个元素为结尾的最长turbulent substring的长度，最后扫描完成之后再取 :math`p_i` 的最大值。

那么 :math:`p_i` 和前面的项有什么关系呢？首先，第i个数和紧邻的前面的第i-1个数之间只可能有三种大小关系

-   :math:`a_{i - 1} < a_i`

    此时如果 :math:`a_{i - 2} > a_{i - 1}` ，那么第i个数可以接上，变成一个更长的turbulent array，即 :math:`p_i = p_{i - 1} + 1` 。

    如果 :math:`a_{i - 2} = a_{i - 1}` ，那么说明前面只有一个长度为1的 [#]_ turbulent array，那么第i个数还是可以接上，变成一个更长的turbulent array，即 :math:`p_i = p_{i - 1} + 1` 。

    如果 :math:`a_{i - 2} < a_{i - 1}` ，那么说明前面形成了长度为 :math:`p_{i - 1}` 的turbulent array，但是可惜第i个数没办法接上去形成一个更长的turbulent array，只能从 :math:`a_{i - 1}` 重新开始，形成一个长度为2的turbulent array，即 :math:`p_i = 2`

-   :math:`a_{i - 1} = a_i`

    直接不用看其他的了，直接就是 :math:`p_i = 1`

-   :math:`a_{i - 1} > a_i`

    情况和 :math:`a_{i - 1} < a_i` 时的情况完全相反。不谈了。

.. [#] 注意，长度为1的array也算turbulent array的。
"""

from typing import *

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        elif len(A) == 2:
            if A[0] != A[1]:
                return 2
            else:
                return 1
        else:
            # if A[0] == A[1]:
            #     dp = [(1, None)]
            # elif A[0] < A[1]:
            #     dp = [(2, True)]
            # else: # A[0] > A[1]
            #     dp = [(2, False)]
            
            # for i, v in enumerate(A[2: ], 2):
            #     if A[i - 1] == v: # flat
            #         dp.append((1, None))
            #     elif A[i - 1] < v: # up
            #         if dp[-1][1] == False: # previous down
            #             dp.append((dp[-1][0] + 1, True))
            #         # elif dp[-1][1] == None:
            #             # dp.append((2, True))
            #         else:
            #             dp.append((2, True))
            #     else: # down
            #         if dp[-1][1] == True: # previous up
            #             dp.append((dp[-1][0] + 1, False))
            #         else:
            #             dp.append((2, False))
            
            # # print(dp)
            # return max(dp, key=lambda v: v[0])[0]

            if A[0] == A[1]:
                dp = [1]
            elif A[0] < A[1]:
                dp = [2]
            else: # A[0] > A[1]
                dp = [2]

            for i, v in enumerate(A[2: ], 2):
                if A[i - 1] == v: # flat
                    dp.append(1)
                elif A[i - 1] < v: # up
                    if A[i - 2] > A[i - 1]:
                        dp.append(dp[-1] + 1)
                    # elif A[i - 2] == A[i - 1]:
                    #     dp.append(2)
                    else: # A[i - 2] < A[i - 1]
                        dp.append(2)
                else: # A[i - 1] > v
                    if A[i - 2] < A[i - 1]:
                        dp.append(dp[-1] + 1)
                    # elif A[i - 2] == A[i - 1]:
                    #     dp.append(2)
                    else: # A[i - 2] > A[i - 2]
                        dp.append(2)

            return max(dp)

# s = Solution()
# assert s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]) == 5
# assert s.maxTurbulenceSize([4,8,12,16]) == 2
# assert s.maxTurbulenceSize([100]) == 1