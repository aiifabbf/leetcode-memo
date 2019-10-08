"""
.. default-role:: math

给一个array，找到公差为 ``difference`` 的最长等差subsequence的长度。

用动态规划吧，假设 ``dp[i]`` 是以第 `i` 个元素结尾的、公差为 ``difference`` 的最长等差subsequence的长度。那么 ``dp[i]`` 和前面的项有什么关系呢？

假如在 `[0, i - 1]` 范围内能找到一个比 ``array[i]`` 正好小一个 ``difference`` 的 ``array[j]`` ，那么 ``array[i]`` 就可以接到 ``array[j]`` 后面，这样 ``dp[i] == dp[j] + 1`` ；如果能找到多个 ``array[j]`` ，取 ``dp[j]`` 最大的那个；如果找不到， ``array[i]`` 就只能单独成一个数列了，所以 ``dp[i] == 1`` 。

如果每次都往前扫描一遍的话，复杂度是 `O(n^2)` ，可以用hash map优化到 `O(n)` ：类似2 sum，用一个hash map，key存前面见过的 ``array[j]`` 值，value存 ``j`` ，这样每次 `O(1)` 就能知道前面存不存在一个 ``array[j]`` 正好能使得 ``array[i] - difference == array[j]`` 了。
"""

from typing import *

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen = {} # key是之前见过的array[j]，value是j
        dp = []

        for i, v in enumerate(arr):
            if v - difference in seen: # 如果之前见过一个array[j]使得array[i] - difference == array[j]
                dp.append(dp[seen[v - difference]] + 1) # 那么array[i]可以接到array[j]后面
            else: # 没见过
                dp.append(1) # 那没办法了，array[i]只能单独成一个数列了
            seen[v] = i # 万一之前见过array[i]了怎么办？直接覆盖不会出问题吗？其实不会的，因为越靠右dp肯定越大。不过如果不放心的话，还是比较一下

        return max(dp)

# s = Solution()
# print(s.longestSubsequence([1, 2, 3, 4], 1))
# print(s.longestSubsequence([1, 3, 5, 7], 1))
# print(s.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))