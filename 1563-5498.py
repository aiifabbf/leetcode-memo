"""
.. default-role:: math

Stone game最新力作！这次的规则是，Alice选一个切点 `i` ，计算出 ``array[..i]`` 的累加和、 ``array[i..]`` 的累加和，Bob会拿走累加和大的那一堆，然后Alice的分数是小的那堆的累加和，然后比赛继续在小的那堆里进行。具体来说，

-   如果 ``array[..i]`` 的累加和比较大，那么Bob会拿走 ``array[..i]`` ，留下 ``array[i..]`` 给Alice，Alice的分数就加上 ``array[i..]`` 的累加和，然后游戏继续在 ``array[i..]`` 里进行。
-   如果 ``array[i..]`` 的累加和比较大，那么Bob会拿走 ``array[i..]`` ，留下 ``array[..i]`` 给Alice，Alice的分数就加上 ``array[..i]`` 的累加和，然后游戏继续在 ``array[..i]`` 里进行。
-   如果一样大，那么Alice来选择留下 ``array[..i]`` 还是 ``array[i..]`` 。
-   如果 ``array`` 已经只剩下一个元素了，那么Alice不得分，游戏结束。

问Alice最多能拿多少分。

递推式很容易写出来，但是计算图里有很多重复节点，所以再加个cache就搞定了。
"""

from typing import *

import itertools
import functools


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        integrals = [0] + list(itertools.accumulate(stoneValue))

        @functools.lru_cache(None)
        def opt(left, right):
            if right - left == 1:
                return 0
            else:
                res = 0

                for middle in range(left + 1, right):
                    a = integrals[right] - integrals[middle]
                    b = integrals[middle] - integrals[left]
                    if a < b:
                        res = max(res, a + opt(middle, right))
                    elif a > b:
                        res = max(res, b + opt(left, middle))
                    else:
                        res = max(res, a + opt(middle, right),
                                  b + opt(left, middle))

                return res

        return opt(0, len(stoneValue))


s = Solution()
print(s.stoneGameV([6, 2, 3, 4, 5, 5]))  # 18
print(s.stoneGameV([7, 7, 7, 7, 7, 7, 7]))  # 28
print(s.stoneGameV([4]))  # 0
