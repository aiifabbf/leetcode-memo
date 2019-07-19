"""
.. default-role:: math

给两个只由 ``X, R, L`` 组成的字符串，定义一次move是

-   把某个 ``XL`` 替换成 ``LX``
-   或者把某个 ``RX`` 替换成 ``XR``

问其中一个字符串经过若干次move之后，能否变成另一个字符串。

其实 ``L`` 的意思就是只能向左移动， ``R`` 的意思就是只能向右移动。题目的意思可以转换成3个等价条件

-   ``start`` 里面从左往右第 `k` 个 ``L`` 的下标必须大于等于 ``end`` 里面第 `k` 个 ``L`` 的下标

    因为 ``L`` 只可以向左移动，所以 ``start`` 里面每个 ``L`` 都只能恰好出现在它对应的 ``end`` 中的 ``L`` 的同一个位置上、或者出现在它的右边，这样这个 ``L`` 才能在某次move中向左移动。

-   ``start`` 里面从左往右第 `k` 个 ``R`` 的下标必须小于等于 ``end`` 里面第 `k` 个 ``R`` 的下标

    和 ``L`` 同理。

-   ``start`` 和 ``end`` 剔除掉 ``X`` 之后剩下的字符串必须相等

    上面两个条件只能保证对应的 ``L`` 和 ``R`` 的相对位置，如果没有这个条件，可能会出现下面这种情况

    ::

        X L R L R <- start
        L L X R R <- end

    这种情况下，上面两个条件是满足的，但是因为 ``L`` 和 ``R`` 不能互相穿越，也就是 ``RL`` 不能替换成 ``LR`` ，所以不能转换。
"""

from typing import *

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        lPositionsInStart = (i for i, v in enumerate(start) if v == "L") # start中所有的L的下标。用generator会节省一次遍历，还可以省内存
        rPositionsInStart = (i for i, v in enumerate(start) if v == "R") # start中所有的R的下标
        lPositionsInEnd = (i for i, v in enumerate(end) if v == "L") # end中所有的L的下标
        rPositionsInEnd = (i for i, v in enumerate(end) if v == "R") # end中所有的R的下标

        if start.replace("X", "") == end.replace("X", "") and all(i >= j for i, j in zip(lPositionsInStart, lPositionsInEnd)) and all(i <= j for i, j in zip(rPositionsInStart, rPositionsInEnd)): # 3条等价条件都满足的话
            return True # 可以转换
        else: # 否则不能转换
            return False

# s = Solution()
# print(s.canTransform("RXXLRXRXL", "XRLXXRRLX")) # true
# print(s.canTransform("XXRXXLXXXX", "XXXXRXXLXX")) # false