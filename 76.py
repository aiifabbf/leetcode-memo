# 找到 ``S`` 中的一个substring，使得这个substring里含有 ``T`` 中所有的字符。返回满足这个要求的最短的substring。

# 题目还钦定一定要 :math:`O(n)` 复杂度。

from typing import *

import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 一改：好像要考虑重复……题干没说啊
        # 二改：Counter太慢了。考虑不要每次都重新生成Counter，增量更新。
        if len(s) < len(t):
            return ""

        # setS = set(s)
        # setT = set(t)
        # if not setT.issubset(setS): # 如果T都不是S的子集，那么再怎么样都根本不可能找到这种窗口
        #     return ""
        counterS = collections.Counter(s)
        counterT = collections.Counter(t)
        if any(counterS[i] < counterT[i] for i in counterT): # 用来对付ccab, aab这种test case
            return ""

        # 至此，排除了不存在window的可能，即从此开始，s一定包含这样一个window了，下面问题转换成找到最短window

        minimumWindowLength = len(t) # 因为要考虑重复，所以最小窗口长度是t的长度
        left = 0 # [left, right)
        right = left + minimumWindowLength
        minimumWindow = s
        counterWindow = collections.Counter(s[left: right])
        while right <= len(s) and right - left >= minimumWindowLength: # 循环条件
            if all(counterWindow[i] >= counterT[i] for i in counterT): # 存在这样一个window
                minimumWindow = min((minimumWindow, s[left: right]), key=len) # 和已有的window对比长度，取短的那个
                if right - left == minimumWindowLength:
                    counterWindow[s[left]] -= 1
                    if right != len(s):
                        counterWindow[s[right]] += 1
                    right += 1
                    left += 1
                else:
                    counterWindow[s[left]] -= 1
                    left += 1
            else: # 不存在
                if right != len(s):
                    counterWindow[s[right]] += 1
                right += 1 # 往右一格

        return minimumWindow

        # 还是很慢。但是至少能过。再说吧。

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "aa"))
print(s.minWindow("ab", "b"))
print(s.minWindow("ccab", "aab"))