"""
用一种方法压缩字符串，把重复的字符用出现的次数代替。出现了一次的后面不跟数字。比如 ``aabbccc`` 变成 ``a2b2c3`` 、 ``abbbbb`` 变成 ``ab5`` 。

我的是传统的那种分块的做法，遍历所有的字符，并且判断当前字符和上次见到的字符是否一样，如果不一样，就认为前面字符块结束了；如果一样，啥也不做。

题目要求用 :math:`O(1)` 空间，但是我没想出来，只能想出 :math:`O(n)` 空间的。
"""

from typing import *

class Solution:
    def compress(self, chars: List[str]) -> int:
        # counter = collections.Counter(chars)
        # return sum(map(lambda v: v if v == 1 else 1 + len(str(v)), counter.values()))
        # 没看清题目要求
        res = []
        lastChar = chars[0] # 前一个字符块的字符
        lastCharPosition = 0 # 前一个字符块的起始位置

        for i, v in enumerate(chars[1: ] + ["\x00"], 1): # 最后追加一个dummy char，省得出迭代之后再处理
            if v != lastChar: # 发现当前字符和前面不一样了，说明出现断层
                if i - lastCharPosition == 1: # 说明前一个字符只出现了一次
                    res.append(lastChar) # 只要追加这个字符，不要追加出现次数
                else: # 说明前一个字符出现了大于等于2次
                    res.append(lastChar) # 追加这个字符
                    res.extend(str(i - lastCharPosition)) # 追加出现的次数
                lastChar = v 
                lastCharPosition = i

        chars[:] = res # 也算modify in place吧
        # print(res)
        return len(res)

# s = Solution()
# print(s.compress(["a","a","b","b","c","c","c"])) # 6
# print(s.compress(["a"])) # 1
# print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])) # 4