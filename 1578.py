"""
给个字符串，删掉一些字符，使得字符串里不存在连续相同的字符。删除位于 `i` 的字符的花费是 ``cost[i]`` ，问最小花费是多少。

比如给

::

    a b a a c
    1 2 3 4 5

必须删掉第2个或第3个 ``a`` 才能使得字符串里没有两个相邻的 ``a`` 。删掉第2个 ``a`` 只要花费3，而删掉第3个 ``a`` 要花费4，所以删掉第2个 ``a`` 更合算。

详细解释在Rust版里。很简单，用一个stack保存 **需要保留的字符** ，每次进来一个新的字符，和stack顶端的字符对比，如果不同，直接放进去；如果相同，保留价值大的字符。
"""

from typing import *


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        stack = []

        for i, v in enumerate(s):
            if len(stack) == 0:
                stack.append((i, v))
            else:
                if stack[-1][1] != v:
                    stack.append((i, v))
                else:
                    that = stack[-1][0]
                    this = i
                    if cost[that] < cost[this]:
                        stack.pop()
                        stack.append((i, v))

        return sum(cost) - sum(cost[i] for i, v in stack)


s = Solution()
print(s.minCost("abaac", [1, 2, 3, 4, 5]))  # 3
print(s.minCost("abc", [1, 2, 3]))  # 0
print(s.minCost("aabaa", [1, 2, 3, 4, 1]))  # 2
