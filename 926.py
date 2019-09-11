r"""
给一个全是 ``0, 1`` 组成的字符串，可以把其中的某些 ``0`` 变成 ``1`` 、``1`` 变成 ``0`` 使得字符串代表的数列变成单调递增的，问最少做多少次这种操作就可以达成目标。

啥意思呢，就是假设原来有个字符串 ``00110`` ，代表数列 `0, 0, 1, 1, 0` ，可以把最后一个 ``0`` 变成 ``1`` ，这样数列就变成了 `0, 0, 1, 1, 1` ，是单调递增的了。当然你也可以把所有的 ``1`` 变成 ``0`` ，从而把整个数列变成 `0, 0, 0, 0, 0` ，但是这样就需要2步操作，不是最优操作了。

思考一下发现，对于一个长度为 `n` 的字符串，翻转之后满足条件的字符串其实只有 `n + 1` 个字符串。比如对于长度为5的字符串，满足条件的只有

::

    00000
    00001
    00011
    00111
    01111
    11111

6种情况。暴力做法是，把原字符串和这6个“模板”字符串一个一个字符比较，就可以得到需要多少步操作，取出最小的那种，但是这样做复杂度是 `O(n^2)` 。按题目要求应该是过不了的。题目暗示要找到一种 `O(n)` 或者 `O(n \ln n)` 的做法。

那么能不能不要和模板字符串一个一个字符地比较呢？能不能做到 `O(1)` 复杂度完成对一个模板的比较？可以的。

仔细观察第0个模板 ``00000`` ，因为全是 ``0`` ，要把原字符串变成这个模板，需要把所有的 ``1`` 都翻转成 ``0`` ，所以就是数出原字符串里 ``1`` 的个数。

观察第1个模板 ``00001`` ，这次不是全 ``0`` 了。要把原字符串变成这个模板，需要分两部分

-   把原字符串前面的4个字符里含有的 ``1`` 全部翻转成 ``0``
-   把原字符串后面的1个字符里含有的 ``0`` 全部翻转成 ``1``

也就是说要

-   数出原字符串从前开始数的4个字符里面 ``1`` 的个数
-   数出原字符串从后开始数的1个字符里面 ``0`` 的个数

是不是突然又转换成求区间和的问题了？给array做一次积分， ``integral[j] - integral[i]`` 就是 ``array[i: j]`` 中 ``1`` 的个数；有了 ``1`` 的个数， ``0`` 的个数也好求， 直接就是substring的长度 ``j - i`` 减去substring中 ``1`` 的个数就是了： ``(j - i) - (integral[j] - integral[i])`` 。

推广一下，对于第 `k` 个模板

::

    000...000 111...111
              ^-------^ k个1

需要

-   数出前半substring，也就是 ``array[: len(array) - k]`` 中 ``1`` 的个数
-   数出后半substring，也就是 ``array[len(array) - k: ]`` 中 ``0`` 的个数

这样就做到了 `O(1)` 做一次模板比较，因为要做 `n + 1` 次比较，所以总的复杂度是 `O(n + 1) = O(n)` 。
"""

from typing import *

import itertools

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        integrals = [0] + list(itertools.accumulate(map(int, S))) # 积分，这样integrals[j] - integrals[i]就是array[i: j]中1的个数
        res = float("inf") # 存最小cost

        for i in range(0, len(S) + 1): # 总共有n + 1个模板，i表示模板中0和1交界的位置
            oneCountInLeftHalf = integrals[i] - integrals[0] # 左半边array[: i]有多少个1
            zeroCountInRightHalf = (len(S) - i) - (integrals[-1] - integrals[i]) # 右半边array[i: ]有多少个0
            cost = oneCountInLeftHalf + zeroCountInRightHalf # 为了把字符串变成模板需要做多少次翻转，也就是cost
            res = min(res, cost)

        return res

# s = Solution()
# print(s.minFlipsMonoIncr("00110")) # 1
# print(s.minFlipsMonoIncr("010110")) # 2
# print(s.minFlipsMonoIncr("00011000")) # 2