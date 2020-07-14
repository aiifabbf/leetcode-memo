"""
.. default-role:: math

array里有多少个全是1的substring（要连续）

如果不会DP也可以做，挑出array里每个连续都是1的substring，一个长度是 `n` 的全1 substring一共有 `1 + 2 + 3 + ... + n` 个全1的substring。

用DP做挺好的。设 ``dp[i]`` 是以第 `i - 1` 个元素结尾的、全是1的substring的个数，如果 ``a[i - 1]`` 是0的话，以 ``a[i - 1]`` 结尾的、全是1的substring的个数当然是0；如果 ``a[i - 1]`` 是1的话，首先它本身可以构成一个长度为1的substring，其次它可以接在每一个以 ``a[i - 2]`` 结尾的全1 substring后面。以 ``a[i - 2]`` 结尾的全1 substring的个数正好又是 ``dp[i - 1]`` ，所以这时候 ``dp[i] = dp[i - 1] + 1`` 。
"""


from typing import *


class Solution:
    def numSub(self, s: str) -> int:
        dp = [0] * (len(s) + 1) # dp[i]表示以a[i - 1]结尾的、全是1的substring的个数

        for i in range(1, len(s) + 1):
            if s[i - 1] == "0":
                dp[i] = 0 # 只能从这里断开了
            else:
                dp[i] = dp[i - 1] + 1 # 可以接在每一个以a[i - 2]结尾的、全1的substring的后面。以a[i - 2]结尾的全1 substring的个数又是dp[i - 1]，所以dp[i] = dp[i - 1] + 1

        return sum(dp) % (10 ** 9 + 7)


s = Solution()
print(s.numSub("0110111"))  # 9
print(s.numSub("101"))  # 2
print(s.numSub("111111"))  # 21
