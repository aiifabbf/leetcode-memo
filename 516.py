"""
找到一个string里的最长回文subsequence（可以不连续）的长度

最简单、最好理解的方法是用“最长公共subsequence（可以不连续）”来解决，也就是归约。

详细的解释在Rust版本里。
"""

from typing import *


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestPalindromeSubsequenceLength(list(s), list(s)[:: -1])

    def longestPalindromeSubsequenceLength(self, s: List, t: List) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(1, len(s) + 1):

            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


s = Solution()
print(s.longestPalindromeSubseq("bbbab"))  # 4
print(s.longestPalindromeSubseq("cbbd"))  # 2
