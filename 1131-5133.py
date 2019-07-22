r"""
.. default-role:: math

给两个array ``a, b`` ，问

.. math::

    \max\{|a_i - a_j| + |b_i - b_j| + |i - j| | 0 \leq i, j \leq n - 1\}

可以看做是求一个三维点集中的点之间的最大曼哈顿距离，两个三维空间中的点 `x = (x_1 x_2 x_3), y = (y_1, y_2, y_3)` 之间的曼哈顿距离就是每一维求差的绝对值、再加和

.. math::

    |x_1 - y_1| + |x_2 - y_2| + |x_3 - y_3|

这个问题里可以把 ``a`` 看成所有点的第一维、 ``b`` 看成第二维、 ``[0, 1, 2, 3, ..., n - 1]`` 看成第三维。那么 ``a[i]`` 就是第 `i` 个点的第一维、 ``b[i]`` 是第 `i` 个点的第二维、``i`` 是第 `i` 个点的第三维。

我知道 `O(n)` 是可以求点集中任意两个点之间的最小距离的，用分治法，所以 `O(n)` 应该也是可以求任意两点之间的最大距离的。但是这个我还不会……

那么能不能考虑去掉绝对值符号，这样好像需要讨论 `2^3 = 8` 种情况，有点多。但是观察到 `f(i, j) = f(j, i)` 所以可以限制 `i < j` ，这样 `|i - j| = j - i` ，只要讨论 `2^2 = 4` 种情况了，那就开始快乐讨论吧

.. math::

    f(i, j) = \begin{cases}
        (a_i + b_i - i) - (a_j + b_j - j), & a_i > a_j, b_i > b_j \\
        (a_j - b_j + j) - (a_i - b_i + i), & a_i < a_j, b_i > b_j \\
        (a_i - b_i - i) - (a_j - b_j - j), & a_i > a_j, b_i < b_j \\
        (a_j + b_j + j) - (a_i + b_i + i), & a_i < a_j, b_i < b_j
    \end{cases}

因为 `|a - b| = \max\{a - b, b - a\}` ，所以 `f(i, j)` 是这4种情况最大的值，所以还可以写成

.. math::

    f(i, j) = \max\left\{
        \begin{aligned}
            (a_i + b_i - i) - (a_j + b_j - j), & a_i > a_j, b_i > b_j \\
            (a_j - b_j + j) - (a_i - b_i + i), & a_i < a_j, b_i > b_j \\
            (a_i - b_i - i) - (a_j - b_j - j), & a_i > a_j, b_i < b_j \\
            (a_j + b_j + j) - (a_i + b_i + i), & a_i < a_j, b_i < b_j
        \end{aligned}
    \right\}

令

.. math::

    \begin{aligned}
        x_i &= - (a_i + b_i - i) \\
        y_i &= a_i - b_i + i \\
        z_i &= - (a_i - b_i - i) \\
        w_i &= a_i + b_i + i
    \end{aligned}

`f(i, j)` 就可以写成和四个数列相关的最大值的形式

.. math::

    f(i, j) = \max\{x_j - x_i, y_j - y_i, z_j - z_i, w_j - w_i\}

而在 `Best Time to Buy and Sell Stock <https://leetcode.com/problems/best-time-to-buy-and-sell-stock/>`_ 里，我们已经知道怎么处理

.. math::

    \max\{a_j - a_i | 0 \leq i < j \leq n - 1\}

了，所以这里直接就可以用啦。

可惜，这样做是不对的，因为第一个限制条件 `i < j` ，使得

.. math::

    \max\{\max\{x_j - x_i, y_j - y_i, z_j - z_i, w_j - w_i\} | 0 \leq i < j \leq n - 1\}

并不等价于

.. math::

    \max\{\max\{x_j - x_i | 0 \leq i < j \leq n - 1\}, \max\{y_j - y_i | 0 \leq i < j \leq n - 1\}, ...\}

因为 `\max` 的结合律只在 `0 \leq i, j \leq n - 1` 时成立。

所以这一题要去掉绝对值符号、讨论8种情况

.. math::

    \begin{aligned}
        x_i &= + a_i + b_i + i \\
        y_i &= + a_i + b_i - i \\
        z_i &= + a_i - b_i + i \\
        w_i &= + a_i - b_i - i \\
        u_i &= - a_i + b_i + i \\
        v_i &= - a_i + b_i - i \\
        s_i &= - a_i - b_i + i \\
        t_i &= - a_i - b_i - i
    \end{aligned}

虽然要讨论8种情况，不过因为没有了 `i < j` 的限制，所以可以利用 `\max` 的结合律了

.. math::

    \begin{aligned}
        & \max\{f(i, j) | 0 \leq i, j \leq n - 1\} \\
        = & \max\{\max\{x_i - x_j, y_i - y_j, ...\} | 0 \leq i, j \leq n - 1\} \\
        = & \max\{\max\{x_i - x_j\}, \max\{y_i - y_j\}, ...\} \\
        = & \max\{\max\{x_i\} - \min\{x_i\}, \max\{y_i\} - \min\{y_i\}, ...\}
    \end{aligned}

其中第二步到第三步利用了

.. math::

    \begin{aligned}
        \max\{a_i - a_j\} &= \max\{a_i\} + \max\{- a_j\} \\
        &= \max\{a_i\} - \min\{a_j\}  \\
        &= \max\{a_i\} - \min\{a_i\}
    \end{aligned}

所以最终结果就是对每个数列 `\{x_n\}, \{y_n\}, ...` 分别求数列里的最大值减最小值，再取所有数列的这个差值的最大值

.. math::

    \max\left\{
        \begin{aligned}
            & \max\{x_i\} - \min\{x_i\}, \\
            & \max\{y_i\} - \min\{y_i\}, \\
            & \vdots \\
            & \max\{t_i\} - \min\{t_i\}
        \end{aligned}
    \right\}
"""

from typing import *

import itertools

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # iterators = []

        # for i in {1, -1}:
        #     for j in {1, -1}:
        #         for k in {1, -1}:
        #             iterators.append(map(lambda v: v[0] * i + v[1] * j + v[2] * k, zip(arr1, arr2, range(len(arr1))))) 
        # 这里坑了，因为作用域的问题，map在迭代过程中i, j, k始终是-1, -1, -1
        
        res = float("-inf")

        for i, j, k in itertools.product({-1, 1}, {-1, 1}, {-1, 1}): # 8种情况分别讨论
            iterator = map(lambda v: v[0] * i + v[1] * j + v[2] * k, zip(arr1, arr2, range(len(arr1)))) # 每种情况对应一个数列
            maximum = float("-inf") # 数列里的最大值
            minimum = float("inf") # 数列里的最小值
            
            for v in iterator:
                if v > maximum:
                    maximum = v
                if v < minimum:
                    minimum = v

            res = max(res, maximum - minimum)

        return res

# s = Solution()
# print(s.maxAbsValExpr([1, 2, 3, 4], [-1, 4, 5, 6])) # 13
# print(s.maxAbsValExpr([1, -2, -5, 0, 10], [0, -2, -1, -7, -4])) # 20
# print(s.maxAbsValExpr([10,5,2,-1,5,1], [-5,-4,2,9,-8,-5])) # 28