"""
.. default-role:: math

一个长度为 `n` 的字符串里只有 ``a, i, u, e, o`` ，但是它们之间的顺序有限制

-   ``a`` 后面只能跟 ``e``
-   ``i`` 后面只能跟 ``a, u, e, o``
-   ``u`` 后面只能跟 ``a``
-   ``e`` 后面只能跟 ``a, i``
-   ``o`` 后面只能跟 ``i, u``

问这个字符串有多少种可能的情况。

还是动态规划。假设

-   ``dpa[i]`` 表示长度为 `i` 的、以 ``a`` 结尾的字符串的个数
-   ``dpi[i]`` 表示长度为 `i` 的、以 ``i`` 结尾的字符串的个数
-   ``dpu[i]`` 表示长度为 `i` 的、以 ``u`` 结尾的字符串的个数
-   ``dpe[i]`` 表示长度为 `i` 的、以 ``e`` 结尾的字符串的个数
-   ``dpo[i]`` 表示长度为 `i` 的、以 ``o`` 结尾的字符串的个数

他们和前一项 ``dpx[i - 1]`` 之间有什么关系呢？一个一个来考虑

-   后一个字符能接 ``a`` 的，只有以 ``i, e, u`` 结尾的字符串，所以 ``dpa[i] = dpi[i - 1] + dpe[i - 1] + dpu[i - 1]``
-   后一个字符能接 ``i`` 的，只有以 ``e, o`` 结尾的字符串，所以 ``dpi[i] = dpe[i - 1] + dpo[i - 1]``
-   后一个字符能接 ``u`` 的，只有以 ``i, o`` 结尾的字符串，所以 ``dpu[i] = dpi[i - 1] + dpo[i - 1]``
-   后一个字符能接 ``e`` 的，只有以 ``a, i`` 结尾的字符串，所以 ``dpe[i] = dpa[i - 1] + dpi[i - 1]``
-   后一个字符能接 ``o`` 的，只有以 ``i`` 结尾的字符串，所以 ``dpo[i] = dpi[i - 1]``

相当于是要把条件反过来想，不是想某个字符后面能跟哪些字符，而是想如果要接某个字符，前面结尾的字符可以有哪些。

实际写的时候，还是不要建 ``dpa, dpi, dpu, dpe, dpo`` 了，太麻烦了，直接用一个hash map来存就好了， ``counter["a"]`` 就表示 ``dpa[i]`` ，然后一轮一轮迭代下去就好了，迭代 `n - 1` 轮。
"""

from typing import *

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5
        else:
            counter = {
                "a": 1,
                "i": 1,
                "u": 1,
                "e": 1,
                "o": 1
            } # dpa[1] = 1, dpi[1] = 1, ..., dpo[1] = 1

            for _ in range(n - 1):
                a, i, u, e, o = map(counter.__getitem__, "aiueo") # 一下子得到dpa[i - 1], dpi[i - 1], ..., dpo[i - 1]
                counter["a"] = e + i + u # dpa[i] = dpe[i - 1] + dpi[i - 1] + dpu[i - 1]
                counter["i"] = e + o
                counter["u"] = i + o
                counter["e"] = a + i
                counter["o"] = i

        return sum(counter.values()) % (10**9 + 7)

# s = Solution()
# print(s.countVowelPermutation(1)) # 5
# print(s.countVowelPermutation(2)) # 10
# print(s.countVowelPermutation(5)) # 68