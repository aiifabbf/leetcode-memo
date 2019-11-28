r"""
.. default-role:: math

给一个字符串、一个字典，问能不能用字典里面的词语拼接出字符串，每个词语可以用无限多次。

反过来想，就是问这个字符串能不能拆成字典里面的词语。暴力做法就是尝试每一种拆法，然后看每种拆法里的每个substring在不在字典里。一个长度为 `n` 的字符串有 `O(2^n)` 种拆法，所以肯定是不行的。

那来考虑一下这里面出现了哪些重复操作。我想了很久，发现并不能找到这里面有什么重复操作。

那么只能从“能否拆词”这件事本身来考虑了。一个字符串 ``s`` 能够完全用字典里面的词语拼接起来的充分必要条件是什么？是存在一个下标 ``0 <= i < len(s)`` 使得

-   ``s[0: i]`` 也能够完全用字典里的词拼接起来
-   并且 ``s[i: ]`` 本身在字典里面

画个图

::
                  /---\ 这一段在字典里
    xxxxxxx.....xxyyyyy
    ^------------^ 这一段能拆

这样就能想到用DP来做了。设 ``dp[j]`` 表示 ``s[0: j]`` 这个substring是否能拆。考虑一下 ``dp[j]`` 怎样用前面的项来表示。

很简单，遍历 `i \in [0, j)` ，如果发现

-   ``s[0: i]`` 能拆，也就是 ``dp[i] == True``
-   并且 ``s[i: j]`` 在字典里

就说明 ``s[0: j]`` 也能拆，所以设 ``dp[j] = True`` 。

如果遍历完了都没有发现能满足上面两个条件的 `i` ，说明 ``s[0: j]`` 不能拆，所以只能设 ``dp[j] = False`` 了。

这样复杂度是 `O(n^2)` 。
"""

from typing import *

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] # dp[i]表示s[0: i]是否能分块。初始条件是s[0: 0]可拆、也就是dp[0] == True
        dictionary = set(wordDict) # 用set来表示字典，这样判断substring在不在字典里的复杂度是O(1)

        for j in range(1, len(s) + 1): 

            for i in range(0, j): # 遍历i in [0, j)，想办法找到一个i使得s[0: i]可拆、并且s[i: j]在字典里
                if s[i: j] in dictionary and dp[i] == True: # 找到了
                    dp.append(True) # 所以s[0: j]可拆
                    break # 不用继续找了
            else: # 没找到
                dp.append(False) # 说明s[0: j]不可拆

        return dp[-1] # 原问题的解是s是否可拆，也即是s[0: len(s)]是否可拆，所以解是dp[len(s)]

# s = Solution()
# print(s.wordBreak("leetcode", ["leet", "code"])) # true
# print(s.wordBreak("applepenapple", ["apple", "pen"])) # true
# print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) # false