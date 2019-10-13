"""
给一个字符串 ``s`` ，最多能删掉 `k` 个字符，能否使得字符串变成回文字符串？

其实就是变相问你字符串的最长回文subsequence（可以不连续）的长度是多少。得到这个长度之后，再用字符串的长度减去这个长度，就是最少需要删除多少个字符才能使字符串变成回文字符串的数量了，如果这个数量小于等于 `k` ，就说明可以做到最多删除 `k` 字符使得字符串变成回文字符串。

那么怎么解决最长回文subsequence的问题呢？可以转化成求一个字符串和这个字符串颠倒过来之后的最长公共subsequence问题，即求 ``p`` 和 ``p[:: -1]`` 的最长公共subsequence问题。

这个最长公共subsequence的问题我们已经解决过了，用动态规划。
"""

from typing import *

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        maximumPalindromeSubsequenceLength = self.longestCommonSubsequenceLength(list(s), list(s)[:: -1]) # 求字符串的最长回文subsequence的长度
        if len(s) - maximumPalindromeSubsequenceLength <= k: # 字符串原先的长度减去最长回文subsequence的长度，就是最少需要删掉多少个字符能使字符串变成回文字符串的数量，如果这个数量小于等于k，说明可以达到要求
            return True
        else: # 如果大于k，说明做不到
            return False

    def longestCommonSubsequenceLength(self, A: List[Type], B: List[Type]) -> int: # 求两个array的最长公共subsequence的长度
        A = [0] + A # 前面补一个0，表示空字符
        B = [0] + B # 前面补一个0，表示空字符
        dp = [[0] * len(B) for _ in range(len(A))] # dp[i][j]表示A[:: i + 1]和B[:: j + 1]的最长公共subsequence的长度

        for i, v in enumerate(A[1: ], 1):

            for j, w in enumerate(B[1: ], 1):
                if v == w: # 如果A[i] == B[j]
                    dp[i][j] = dp[i - 1][j - 1] + 1 # 可以追加在A[:: i]和B[:: j]的最长公共subsequence的后面
                else: # 如果A[i] != B[j]
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # 那么目前为止最长的公共subsequence是A[:: i]和B[:: j - 1]的最长公共subsequence、或者是A[:: i - 1]和B[:: j]的最长公共subsequence。

        return dp[-1][-1] # 最终答案是A[::]和B[::]的最长公共subsequence

# s = Solution()
# print(s.isValidPalindrome("abcdeca", 2))