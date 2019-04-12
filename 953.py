"""
字母表不再是 ``a, b, c, d, ..., z`` ，而是变成了一个奇怪的顺序，问一个包含string的array在这个新的字母表下面是否仍然是符合字典顺序的。

我的思路是把string从新的字母表映射到abc字母表，再常规比较就好了。
"""

from typing import *

import string

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {ord(i): ord(v) for i, v in zip(order, string.ascii_lowercase)} # 从新字母表到常规abc字母表的映射表
        translated = [word.translate(mapping) for word in words] # 转换一下
        return translated == sorted(translated) # 看是否是排好序的

# s = Solution()
# assert s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True
# assert s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz") == False
# assert s.isAlienSorted(["ubg","kwh"], "qcipyamwvdjtesbghlorufnkzx") == True