"""
只颠倒字符串里的字母，其他的数字啊符号啊之类的位置不变。

比如 ``Test1ng`` 变成 ``gnt1seT``
"""

from typing import *

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        mapping = [(i, v) for i, v in enumerate(S) if v.isalpha()] # 所有letter的下标和字母
        reversedMapping = list(reversed(mapping)) # 倒过来
        res = list(S)

        for item, reversedItem in zip(mapping, reversedMapping): # 正序和倒序一起遍历，取正序的下标、倒序的字母
            res[item[0]] = reversedItem[1]

        return "".join(res)