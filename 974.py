r"""
.. default-role:: math

给一个array，问这个array有多少个substring（要连续）的和是K的倍数。

暴力做法就是判断每个substring，因为一个长度为 `n` 的array有 `O(n^2)` 个substring，所以复杂度是 `O(n^2)` 。

一开始想到的是DP（flag警告）。设 ``dp[i]`` 是一个 ``dict`` ，key是以第i个元素结尾的所有的substring的和对K的余数，value是以第i个元素结尾的所有和对K的余数是key的substring的个数。比如对于 ``4, 5, 0, -2, -3, 1`` 

::

    dp[0] = {
        4: 1
    },

    dp[1] = {
        0: 1, # 因为5 % 5 = 0
        4: 1, # 因为(4 + 5) % 5 = 4
    },

    dp[2] = {
        0: 2, # 因为0 % 5 = 0, (0 + 5) % 5 = 0
        4: 1, # 因为(4 + 5 + 0) % 5 = 4
    },

    ...

这样就很方便了，结果就是 ``sum(v[0] for v in dp)`` 也就是每个 `dp[i][0]` 全部加起来。时间复杂度大概是 `O(nk)` ，空间复杂度可以优化到 `O(k)` （如果只存前一个 ``dp[i]`` 的话）。

可惜上面的做法是过不了的……因为 `k` 也很大，最大可以30000，所以这题的要求是 `O(n)` 。看了答案，用了积分的做法。

1.  先给A做个积分

    比如给 ``4, 5, 0, -2, -3, 1`` 做积分得到 ``4, 9, 9, 7, 4, 5`` 。

2.  数出积分里面每个累加和对K的余数出现的次数

    比如 ``4, 9, 9, 7, 4, 5`` 先逐个对K求余数，变成 ``4, 4, 4, 3, 4, 0`` ，做一个直方图

    ::

        {
            0: 1,
            3: 1,
            4: 4
        }

3.  思考积分的意义：积分里每一项都代表从第一个元素到当前这个元素的substring的和，所以如果在积分里随便选两项，靠后的一项减去靠前的一项，得到的时候某个substring的和，如果出现某两项相等，说明后面项减前面项等于0，又因为是和对K的余数，也就是说存在一个substring的和对K的余数是0，也就是说存在一个substring的和是K的倍数。

    比如假设出现了这样一种积分 ``1, ..., 1, ..., 1`` ，出现了3项1，那么说明

    -   从第1个1开始到第2个1的这个substring的和对K的余数是0
    -   从第1个1开始到第3个1的这个substring的和对K的余数是0
    -   从第2个1开始到第3个1的这个substring的和对K的余数是0

    总共有3个substring的和是K的倍数。

    推广一下，如果出现 `n` 项相同，那么有多少个substring的和是K的倍数？发现就是等差数列求和，共有

    .. math::

        1 + 2 + 3 + \cdot + (n - 1) = {1 + (n - 1) \over 2} \times (n - 1) = {n (n - 1) \over 2}

    个substring的和是K的倍数。

    所以这就是给积分对K的余数做直方图的意义，我们需要把出现次数大于等于2的积分过滤出来，然后看这些积分可以构造出多少个和对K的余数是0的substring。
"""

from typing import *

import collections
import itertools

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # dp = collections.Counter({A[0] % K: 1})
        # # dp = {A[0] % K: 1}
        # res = 1 if A[0] % K == 0 else 0

        # for i, v in enumerate(A[1: ], 1):
        #     thisDp = collections.Counter({(j + v) % K: w for j, w in dp.items()})
        #     thisDp[v % K] = thisDp[v % K] + 1
        #     res = res + thisDp[0]
        #     dp = thisDp
        #     # 每次都新建一个Counter太慢了

        #     # thisDp = {(j + v) % K: w for j, w in dp.items()}
        #     # thisDp[v % K] = thisDp.get(v % K, 0) + 1
        #     # res = res + thisDp.get(0, 0)
        #     # dp = thisDp
        #     # 用dict并不会快多少

        # return res

        # integral = itertools.accumulate(A) # 给A做个积分
        # counter = collections.Counter(v % K for v in integral) # 数出积分里面每个累加和对K的余数出现的次数
        # return counter[0] + sum(map(lambda w: w[1] * (w[1] - 1) // 2, filter(lambda v: v[1] >= 2, counter.items())))
        # 最好在integral前面加一个dummy 0，这样就不用单独统计0出现的次数了。

        integral = itertools.accumulate(A) # 给A做个积分
        counter = collections.Counter(v % K for v in integral) # 数出积分里面每个累加和对K的余数出现的次数
        counter[0] += 1 # 等效为integral前面加了个dummy 0，这样可以不用把integral从generator变成list，可以省很多内存
        return sum(map(lambda w: w[1] * (w[1] - 1) // 2, filter(lambda v: v[1] >= 2, counter.items()))) # 首先过滤出出现次数大于等于2的积分项，然后用等差数列求和公式算出它们总共能构造出多少个和对K的余数是0的substring

# s = Solution()
# print(s.subarraysDivByK([4, 5, 0, -2, -3, 1], 5)) # 7