"""
.. default-role:: math

从数字里最多删掉 `k` 个数字，使剩下的数字最小

比如 ``1432219`` 里删掉3个数字，选择删掉 ``4, 3, 2`` 之后，数字变成 ``1219`` ，是最小的数字。

要注意类似 ``10200`` 里删1个数字的情况：删掉最前面的 ``1`` 之后，剩下的数字是 ``0200 = 200`` ，所以最小数字是200。

暴力做法是遍历所有情况，复杂度是 `O(C_n^k)` 。

用greedy，从左到右找到第一个满足“右边的数字小于自己”的数字，删掉它。比如 ``1432219`` 第一步就是找到4然后删掉。

有时会找不到，比如 ``12345`` 本身已经是单调递增的了，那么删掉最后一个数字能使得剩下的字符串最小。这样的步骤重复 `k` 次就可以了。复杂度降到了 `O(n^2)` 。

立刻想到可以用单调递增stack使得复杂度降低到 `O(n)` 。pop一次相当于删掉一个数字，所以pop之前还要判断剩余删除机会够不够。
"""

from typing import *

from itertools import dropwhile # python也有drop while


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for v in num:
            while len(stack) > 0 and stack[-1] > v and k > 0:
                stack.pop()
                k -= 1

            stack.append(v)

        while k > 0: # 假如已经是12345了、但是还有剩余删除机会，那么删除最后k个数字
            stack.pop()
            k -= 1

        res = "".join(map(str, dropwhile(lambda v: v == '0', stack)))
        if len(res) == 0:
            return "0"
        else:
            return res


s = Solution()
print(s.removeKdigits("1432219", 3)) # 1219
print(s.removeKdigits("10200", 1)) # 200