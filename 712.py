class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        s1 = "0" + s1
        s2 = "0" + s2
        dp = [[0] * len(s2)]
        for i, row in enumerate(s2[1: ], 1):
            dp.append([0])
            for j, col in enumerate(s1[1: ], 1):
                if s2[i] == s1[j]:
                    dp[-1].append(dp[i - 1][j - 1])
                else:
                    dp[-1].append(min(dp[i - 1][j] + ord(s1[i]), dp[i][j - 1] + ord(s2[j])))
        return dp[-1][-1]

Solution().minimumDeleteSum("sea", "eat")