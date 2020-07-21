r"""
.. default-role:: math

Alice和Bob玩一种游戏，Alice先手，Bob后手。游戏规则是这样的，Alice和Bob轮流从一堆石头里面，拿走任意平方数个石头，比如只能拿走1个、4个、9个……石头。一旦谁遇到场上没有石头可拿了，这个人就输。一开始场上有 `n` 个石头，问Alice能不能赢。

设 `f(i)` 是场面上有 `i` 个石头、Alice先手的时候Alice有没有必胜策略。比如 `f(1)` 表示场面上有一块石头，而且现在是Alice的回合，Alice有没有必胜策略。

考虑下 `f(i)` 有没有什么好用的性质。这个游戏没有平局，所以要么Alice赢（等价于Bob输）、要么Alice输（等价于Bob赢）。所以 `\neg f(i) 就表示场面上有 `i` 个石头、Alice先手的时候Bob有没有必胜策略，也等价于场面上有 `i` 个石头、Bob先手的时候Alice有没有必胜策略。

现在来考虑怎么确定 `f(i)` ，考虑一下 `f(i)` 的递推式。想象你就是Alice，在面对 `i` 个石头的时候，该拿走几个石头才能赢呢？或者说不管拿走几块石头都不可能赢？

因为游戏规则规定只能拿走平方数个石头，所以Alice的选择其实并不多，这一回合她能拿走的石头的个数的集合是

.. math::

    \{j^2 | i - j^2 \geq 0, j \geq 1\}

假设这一回合Alice拿走了 `j^2` 个石头，那么下一回合留给Bob的就是 `i - j^2` 个石头。如果此时Alice仍然有必胜策略，那么Alice就赢。那么场面上有 `i - j^2` 个石头、Bob先手、Alice有必胜策略的式子是什么呢？是 `\neg f(i - j^2)` 。

所以 `f(i)` 的递推式非常容易写出来

.. math::

    f(i) = \exists j \geq 1, i - j^2 \geq 0: \neg f(i - j^2)

再来考虑初始条件 `f(0)` 应该是true还是false。应该是false，一开始我也搞错了。当场面上没有石头、而又是Alice的回合的时候，Alice没有石头可拿，所以Alice必输，没有必胜策略。
"""

from typing import *

import math


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # else:
        #     m = math.floor(math.sqrt(n))
        #     return any(not self.winnerSquareGame(n - i ** 2) for i in range(1, m + 1))
        # 递归写法，会爆栈

        dp = [False] * (n + 1)
        dp[0] = False # Alice先手、场上一块石头都没有的时候，Alice是输的

        for i in range(1, n + 1):
            m = math.floor(math.sqrt(i))
            dp[i] = any(not dp[i - j ** 2] for j in range(1, m + 1))

        return dp[n]

s = Solution()
print(s.winnerSquareGame(1)) # true
print(s.winnerSquareGame(2)) # false
print(s.winnerSquareGame(3)) # true
print(s.winnerSquareGame(4)) # true
print(s.winnerSquareGame(7)) # false
print(s.winnerSquareGame(17)) # false