r"""
.. default-role:: math

一条传送带上有n个货物，array的第i个元素表示第i个货物的重量，运送货物需要按照传送带从前往后的顺序。需要在最多D天的时间里把货物运完，那么船的载重至少要多少？

..
    题目的意思等效为，把一个array分成n个substring，求出每个substring的和，把最大的和记为S，S的最小值是多少？

    假设这个array是 `{a_k} = a_0, a_1, a_2, ..., a_{n - 1}` ，array的积分序列 `{S_k}` 是

    .. math::

        0, S_1, S_2, S_3, ..., S_n

    也就是要从上面的积分序列 `{S_k}` 里取出 `d - 1` 项 `s_1, s_2, ..., s_{d - 1}` （为啥是 `d - 1` 项呢？因为要保证所有的货物都要运走，所以如果取 `d` 项，最后取出的一项 `s_d` 必须是积分序列的最后一项，即 `s_d = S_n` ，所以也没有必要算在里面了），使得

    .. math::

        \max\{s_1 - 0, s_2 - s_1, s_3 - s_2, ..., s_d - s_{d - 1}\}

    最小，并求出最小值。

    暴力做法就是遍历每一种情况，一共有 `C_n^{d - 1}` 种情况，所以复杂度是 `O(C_n^{d - 1})` 。肯定是过不了的。

.. 哈哈哈没想到我两年之前居然是这么考虑这个问题的。完全连边都没猜到呢……突然感慨这两年好像也知道了许多东西，算是进步了不少？不知道有没有副作用，我已经感觉自己学没学多少，倒已经出现了思维定式。

详细解释在Rust写的版本里，大概是归约到判定表述，然后二分找到能使得判定为真的最小的值。
"""

from typing import *

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(capacity: int) -> bool:
            # 载货量为capacity的货船能不能在最多D天内运完所有货物
            # 观察到，比如说，如果载货量是10的货船，能做到在最多D天内运完所有的货物，那么载货量是11的货船肯定也可以在最多D天内运完所有的货物
            # 所以发现把f(n)的取值写出来，会是0, 0, 0, ..., 0, 1, 1, ...这样子的，一旦出现了一次1之后，后面就全部都是1
            # 这时候用二分找到第一次出现1的n，n就是最小的满足条件的载货量了
            count = 0
            loaded = 0

            for v in weights:
                if loaded + v > capacity:
                    count += 1
                    loaded = v
                else:
                    loaded += v

            if loaded != 0:
                count += 1

            return count <= D

        # 俗套的二分
        target = True
        left = max(weights)
        right = sum(weights) + 1

        while left < right:
            middle = (left + right) // 2
            test = feasible(middle)
            if target < test:
                right = middle
            elif target > test:
                left = middle + 1
            else:
                right = middle

        return left