"""
找到array里最长的、成等差数列的subsequence（不一定连续）的长度

典型DP。用 ``dp[i]`` 这个 ``dict`` 表示所有以第i个元素结尾的等差数列sequence的公差（作为key）和长度（作为value）。每次遍历到一个元素，就往前找，看当前元素能不能追加到前面的某个等差数列上。
"""

from typing import *

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if A:
            dp = [
                # {None: 1}
                {}
            ] # 以第0个元素结尾的等差数列当然长度只有1，那么也没必要存了
            maximumLength = 1

            for i, v in enumerate(A[1: ], 1):
                # temp = {None: 1}
                temp = {} # 以第i个元素结尾的所有等差数列的公差和长度

                # for j in reversed(range(0, i)): # 为什么reserved就不行呢？因为如果出现重复，长度小的会覆盖掉长度大的，如果加一个max那么顺序就没有关系了
                for j in range(0, i): # 往前看能不能接到以第j元素结尾的等差数列里
                    # if v - A[j] in dp[j]:
                    #     temp[v - A[j]] = dp[j][v - A[j]] + 1
                    # else:
                    #     temp[v - A[j]] = 2
                    temp[v - A[j]] = dp[j].get(v - A[j], 1) + 1 # 公差为A[i] - A[j]、以第i个元素结尾的等差数列的最大长度，是公差为A[i] - A[j]、以第j个元素结尾的等差数列的最大长度加一
                    # temp[v - A[j]] = max(dp[j].get(v - A[j], 1) + 1, temp.get(v - A[j], 1))
                    maximumLength = max(maximumLength, temp[v - A[j]]) # 一边遍历一边记录最大长度，省得最后再遍历一遍

                dp.append(temp)

            # print(dp, maximumLength)

            return maximumLength
        else:
            return 0

s = Solution()
assert s.longestArithSeqLength([9,4,7,2,10]) == 3
assert s.longestArithSeqLength([20,1,15,3,10,5,8]) == 4
assert s.longestArithSeqLength([22,8,57,41,36,46,42,28,42,14,9,43,27,51,0,0,38,50,31,60,29,31,20,23,37,53,27,1,47,42,28,31,10,35,39,12,15,6,35,31,45,21,30,19,5,5,4,18,38,51,10,7,20,38,28,53,15,55,60,56,43,48,34,53,54,55,14,9,56,52]) == 6