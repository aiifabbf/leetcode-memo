"""
给一个字符串，输出里面每个字母以大写、小写形式分别出现的所有情况。

比如 ``a1b2`` 里， ``a, b`` 都分别可以是小写或者大写，所有情况就是 ``a1b2, A1b2, a1B2, A1B2`` 这四种。

也还是可以看做是决策树。每次遇到一个字符，如果是数字，就不管；如果是字母，有大写和小写两种选择。题目的目标也就转换成了输出决策树从根节点到叶子的所有路径。
"""

from typing import *

import functools

class Solution:
    @functools.lru_cache() # 会快一点点
    def letterCasePermutation(self, S: str) -> List[str]:
        # if S.isdigit(): # 全数字做一点小优化
        #     return [S]
        # 好吧，还不如不优化，反而更快

        res = []
        if S: # 非空字符串
            if S[0].isalpha(): # 是字母
                lower = S[0].lower() # 小写
                upper = S[0].upper() # 大写
                res += [
                    lower + suffix for suffix in self.letterCasePermutation(S[1: ])
                ] # 这一步选择小写，再继续后面的选择
                res += [
                    upper + suffix for suffix in self.letterCasePermutation(S[1: ])
                ] # 这一步选择大写，再继续后面的选择
            else: # 是数字
                res += [
                    S[0] + suffix for suffix in self.letterCasePermutation(S[1: ])
                ] # 不做变换，直接继续后面的选择
            return res
        else: # 空字符串
            return [S]

# s = Solution()
# print(s.letterCasePermutation("a1b2"))
# print(s.letterCasePermutation("3z4"))
# print(s.letterCasePermutation("12345"))