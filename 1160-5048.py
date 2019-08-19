"""
可以用chars里面的字符（每个字符只能用一次）拼出多少个word？这些word加起来总长度是多少？

用Counter很简单：先统计chars里面每个字符出现的次数，再遍历每个word，统计每个word里每个字符出现的次数，看一下

-   这些字符是不是都是chars里面出现过的字符
-   每个字符出现的次数是否超过chars里面同一个字符出现的次数

如果这两个条件满足，说明这个word是符合条件的。
"""

from typing import *

import collections

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = collections.Counter(chars) # 统计chars里面每个字符出现的次数
        res = 0 # 总长度

        for word in words: # 遍历每个word
            c = collections.Counter(word) # 统计每个word里每个字符出现的次数
            
            for k, v in c.items():
                if k not in counter: # 这个word里出现了一个没有在chars里面出现过的字符
                    break # 所以不符合条件
                elif v > counter[k]: # 这个字符在word里出现的次数超过了在chars里出现的次数
                    break # 同样不符合条件
            else: # 否则符合条件
                res = res + len(word) # 更新总长度

        return res

# s = Solution()
# print(s.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
# print(s.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))