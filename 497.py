r"""
.. default-role:: math

给一些矩形，在这些矩形范围内按均匀分布随机抽样采整数点。

我的做法是先统计出每个矩形范围内整数点的个数，每次抽样之前，先以整数点个数为权重，随机选出一个矩形，然后再在这个矩形的所有整数点里均匀采样。

这样是可以保证均匀的，因为矩形越大，整数点越多，那么当然采样到大矩形范围内的样本的概率越大。

-----

做的时候突然就很好奇带权随机是怎么是实现的，找了一下 <https://stackoverflow.com/questions/1761626/weighted-random-numbers> 发现权重其实是离散概率密度函数，先变成概率分布函数，到采样的时候，先在 `[0, 1)` 之间采一个数，然后去概率分布函数里二分搜索。

举个例子，取 `0, 1, 2, 3 的权重是 `1 / 8, 1 / 4, 1 / 2, 1 / 8` ，离散概率密度函数是

.. math::

    f(x) = \begin{cases}
        {1 \over 8}, & x = 0 \\
        {1 \over 4}, & x = 1 \\
        {1 \over 2}, & x = 2 \\
        {1 \over 8}, & x = 3
    \end{cases}

根据概率分布函数的定义 `F(x) = P(X \leq x)` ，概率分布函数应该是这样的

.. math::

    F(x) = \begin{cases}
        0, & x < 0 \\
        {1 \over 8}, & 0 \leq x < 1 \\
        {3 \over 8}, & 1 \leq x < 2 \\
        {7 \over 8}, & 2 \leq x < 3 \\
        1, & 3 \leq x
    \end{cases}

这时候去 `[0, 1)` 里采样，如果采到了0.1，正好在 `[0, 1 / 8)` 里，所以这时候应该返回0；如果采到了0.9，正好在 `[7 / 8, 1)` 里，所以这时候应该返回3。

用代码实现的话，因为浮点数有误差，而且权重一般都用整数表示（比如袋子里的红球有多少个之类的），假设是 ``weights`` ，先按老规矩算出积分 ``integrals`` 使得 ``integrals[j] - integrals[i] == sum(weights[i: j])`` 。然后在 `[0, \Sigma)` 范围内均匀采样，取一个整数，其中 `\Sigma` 就是 ``sum(weights)`` 。

假设采样到了 `k` ，拿着 `k` 去 ``integrals`` 里二分搜索，找到一个 `a_i` 使得 `k \in [a_i, a_{i + 1})` ，此时 `i` 就是最终样本了。

.. 528就是带权采样。
"""

from typing import *

import random


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rectangles = []
        self.weights = []

        for rectangle in rects:
            lowerLeft = (rectangle[0], rectangle[1])
            upperRight = (rectangle[2], rectangle[3])
            self.rectangles.append((lowerLeft, upperRight))
            self.weights.append(
                (upperRight[1] - lowerLeft[1] + 1) * (upperRight[0] - lowerLeft[0] + 1))  # 注意权重不是矩形的面积，而是矩形里可取的点的个数，因为采样的时候并不是随机投点，而是只能选在矩形范围里的点

    def pick(self) -> List[int]:
        rectangle = random.choices(self.rectangles, self.weights, k=1)[0] # 先按矩形中整数点的数量为权重，选出一个矩形
        lowerLeft, upperRight = rectangle
        return [random.randint(lowerLeft[0], upperRight[0]), random.randint(lowerLeft[1], upperRight[1])] # 再在这个矩形的范围内均匀抽样


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
