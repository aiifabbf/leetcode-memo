"""
美化序列号

没什么好说的，按题目要求来就好了。题目要求从后往前，尽可能数到K个元素凑成一组，然后加一个 ``-`` ；最前面凑不到K个的就保留。
"""

from typing import *

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        array = list(S.replace("-", "").upper()) # 首先要把所有的字母都变成大写字母
        if array:
            res = [] # 已经格式化完成的
            buffer = [] # 暂存

            for v in reversed(array): # 从后往前遍历
                buffer.append(v)
                if len(buffer) == K: # 正好一组
                    res += buffer
                    res.append("-") # 插入一个 ``-``
                    buffer = []

            # 出循环的时候也要考虑一下，因为如果最前面一组正好凑了K个，res里面会多加一个 ``-`` ，要去掉。
            if buffer: # buffer不为空，说明最前面没有正好凑满一组
                res += buffer # 直接加上就好了
            else: # buffer为空，说明最前面正好凑满一组了，res多加了一个 ``-`` ，要去掉
                res.pop() # 去掉最前面的 ``-``
            return "".join(reversed(res))
        else: # 这里有坑，比如给---和3的时候
            return ""

# s = Solution()
# print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
# print(s.licenseKeyFormatting("5F3Z-2e-9-w", 9))
# print(s.licenseKeyFormatting("2-5g-3-J", 2))
# print(s.licenseKeyFormatting("---", 3))