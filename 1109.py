"""
.. default-role:: math

给一个序列

.. math::

    [(i, j, k)]

其中每个tuple都表示给 `a_i, a_{i + 1}, ..., a_{j - 1}, a_j` 每项都加上 `k` 。问最后 `a_1, a_2, ..., a_n` 是多少。

暴力做法就是遍历每个tuple `(i, j, k)` ，然后再遍历 `{a_n}` 把从 `a_i` 到 `a_j` 的每一项都加上 `k` 。假设序列里总共有 `m` 个tuple，所以这样做的复杂度是 `O(mn)` ，会超时。

这种暴力做法有个形象的类比，就是把每个tuple都看做是从 `a_i` 开始横跨到 `a_j` 的、 `a_j - a_i + 1` 个宽度为1、高度为 `k` 的一横排矩形，把它们按顺序覆盖，最后统计每个 `i` 上所有矩形堆起来的高度。

每次遇到这种面积堆起来的题目，就一定要想到积分和微分，这道题也是用微分和积分做的。单个tuple `(i, j, k)` 可以代表一个从 `a_i` 开始、横跨到 `a_j` 的、宽度为 `a_j - a_i + 1` 、高度为 `k` 的矩形。这是从原函数的角度来看的。其实也可以从微分域上看这个 ``bookings[i]`` ，会发现它在微分域上代表两个冲击。

试试给这个矩形做 **微分** ，或者准确点说是做差分，会在 `x = i` 上得到一个宽度为1、高度为 `k` 的冲击，在 `x = j + 1` 上得到一个宽度为1、高度为 `-k` 的冲击。所以其实每个 ``bookings[i]`` 不仅在原函数域上代表一个矩形，从微分域上看，它在微分域上也代表了 **一对冲击** 。又因为微分是线性的，所以把每个 ``bookings[i]`` 代表的冲击加起来，就可以得到原函数的微分。

由于积分是线性操作，所以有2种等价的方法把微分变成原函数

1.  就是原始的方法，先对每个冲击对做积分，变回原函数域，然后再在原函数域上把所有的积分值加起来

    也就是先积分、再加和。其实本质上就是暴力做法。

    对一个冲击对做积分，复杂度是 `O(n)` ；对把m个冲击对的积分加起来，复杂度是 `O(mn)` 。

2.  或者，先把所有的冲击对在微分域上全部加起来，变成原函数的微分，再把整个图像积分，变回原函数域

    也就是先加和、再积分。利用积分和加和操作的交换律。

    把所有冲击对加起来，复杂度是 `O(m)` ，因为有m个冲击对；给微分图像做积分，复杂度是 `O(n)` ，因为积分就是一个累加的操作，只要遍历一遍就可以了。

看到第二种方法明显复杂度低多了。

在Leetcode上也写了篇 `解释 <https://leetcode.com/problems/corporate-flight-bookings/discuss/329271/python-differentiate-and-integrate-perspective>`_

.. code:: markdown

    Let `res` be the result list. The list `bookings` can be seen as representing discrete derivatives (or differences) of `res`:

    For every `bookings[i] = (a, b, d)`, it represents a pair of *spikes*, one positive spike with height=`+d` at `a` and another negative spike with height=`-d` at `b+1`. `bookings` form many spikes, and they represent the derivative of `res`. So when you integrate (or accumulate) the one pair of spikes, you get a rectangular area spanning from `a` to `b` with a height of `d`. This rectangular area is one of the many rectangles that stack upon each other to form the final `res`. So when you integrate all the pairs of spikes, you get the final `res`.

    Due to *linearity* of differentiation and integration operation, whether you choose to

    1. gather all the derivatives together (iterate over `bookings`once, complexity `O(bookings.length)`), then integrate (iterate over `res` once, complexity `O(n)`) to get `res`
    2. or integrate the derivatives one by one (for every `bookings[i]`, iterate over `res` once, complexity `O(bookings.length * n)`), then stack all the rectangles to get `res` (complexity `O(bookings.length * n)`)

    you always get the same `res`, but their time complexity can be hugely different. It seems method 1 is preferable.
"""

from typing import *

import itertools

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        derivatives = [0] * (n + 2)

        for i, j, delta in bookings:
            derivatives[i] += delta
            derivatives[j + 1] -= delta

        return list(itertools.accumulate(derivatives))[1: -1]

# s = Solution()
# print(s.corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))