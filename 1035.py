"""
求最长公共subsequence（可以不连续）的长度

经典动态规划题。为了方便处理空array的情况，各自在A和B前面加一个表示空元素的记号。然后，设 ``dp[i][j]`` 为 ``A[0], A[1], ..., A[i]`` 和 ``B[0], B[1], ..., B[j]`` 的最长公共subsequence的长度。那么 ``dp[i][j]`` 和前面的项有什么关系呢？

-   如果 ``A[i] == B[j]`` ，那么最长公共subsequence可以追加当前元素，所以长度加1，即 ``dp[i][j] = dp[i - 1][j - 1] + 1``
-   如果 ``A[i] != B[j]`` ，情况会复杂一点，此时 ``A[i], B[j]`` 没办法接到之前最长公共subsequence上，所以只有两种选择

    -   取 ``A[0], A[1], ..., A[i - 1]`` 和 ``B[0], B[1], ..., B[j]`` 的最长公共subsequence的长度，即 ``dp[i - 1][j]`` 作为当前最长公共subsequence的长度
    -   或者取 ``A[0], A[1], ..., A[i]`` 和 ``B[0], B[1], ..., B[j - 1]`` 的最长公共subsequence的长度，即 ``dp[i][j - 1]`` 作为当前最长公共subsequence的长度

    那么这两种选择里应该选哪个比较好呢？肯定是选长的那个，这样才符合 ``dp[i][j]`` 的定义。所以此时 ``dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`` 。
"""

from typing import *

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        A = [0] + A
        B = [0] + B # 为了方便处理空array的情况，前面加一个dummy元素
        dp = [[0] * len(B) for _ in range(len(A))] # dp[i][j]初始化为0，因为第一行、第一列都是0（空array当然不管怎样公共subsequence长度都为0）

        for i, v in enumerate(A[1: ], 1):

            for j, w in enumerate(B[1: ], 1):
                if v == w: # A[i] == B[j]
                    dp[i][j] = dp[i - 1][j - 1] + 1 # 可以追加元素，所以长度+1
                else: # A[i] != B[j]
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # 不可以追加元素，只能二选一，选长的

        return dp[-1][-1] # 结果不是max(dp)，而是右下角

# s = Solution()
# print(s.maxUncrossedLines([1, 4, 2], [1, 2, 4])) # 2
# print(s.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2])) # 3