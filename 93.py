"""
从字符串里恢复出可能的IP地址

比如 ``25525511135`` 可能是

::

    255.255.11.135
    255.255.111.35

还有可能给你一个巨长的、根本不可能是IP地址的字符串，比如 ``11111111111111111`` 。

暴力做一下就能过。
"""

from typing import *

import itertools

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 3 * 4: # 如果字符串的长度超过12
            return [] # 别想了，肯定不是IP地址
        else:
            indexesToInsertPoint = itertools.combinations(range(1, len(s)), 3) # 可能插入点的3个位置
            allCombinations = map(lambda v: s[: v[0]] + "." + s[v[0]: v[1]] + "." + s[v[1]: v[2]] + "." + s[v[2]: ], indexesToInsertPoint) # 所有可能的情况
            return list(filter(lambda v: all(0 <= int(v) < 256 and not (v.startswith("0") and len(v) > 1) for v in v.split(".")), allCombinations)) # 所有可能的情况一个一个过滤

# s = Solution()
# print(s.restoreIpAddresses("25525511135"))
# print(s.restoreIpAddresses("010010"))
# print(s.restoreIpAddresses("111" * 100))