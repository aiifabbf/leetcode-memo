r"""
.. default-role:: math

用五个元音字母 ``a, i, u, e, o`` 组成长度为 `n` 、单调递增的字符串能组成几个？

比如组成长度是2的字符串，总共有

::

    aa
    ai
    au
    ae
    ao
    ia
    ii
    iu
    ...
    oo

25种，但其中满足单调递增的字符串没几个

::

    aa
    ai
    au
    ae
    ao
    ee
    ei
    eo
    eu
    ii
    io
    iu
    oo
    ou
    uu

先啥都不要想，就看这个例子，找找规律。

首先第0个字符，随便填哪个都可以。第1个字符开始就有讲究了，ASCII要大于等于前面一个。这意味着，如果第0个填的是 ``a`` ，那么第1个可以填入 ``a, e, i, o, u`` ；如果第0个填的是 ``e`` ，那么第1个字符只能填 ``e, i, o, u`` ，只有四种选择。

所以如果定义个函数 `f(n)` 表示长度为 `n` 的满足条件的字符串有几个，光有一个 `n` 一维参数是不够的。还需要一个 `m` 表示第0个字符的选择空间是什么。假设 `m` 表示第0个字符可以从 ``a, e, i, o, u`` 里面的第 `m` 个字符开始选，那么从刚才的例子里可以看到

.. math::

    f(2, 0) = f(1, 0) + f(1, 1) + f(1, 2) + f(1, 3) + f(1, 4) + f(1, 5)

`f(2, 0)` 表示长度为2、第0个字符可以从 ``a, e, i, o, u`` 里选，总共有多少种方式。 `f(1, 1)` 表示长度为1、第0个字符可以从 ``e, i, o, u`` 里选，总共有多少种方式。

这样递推式很容易就出来了

.. math::

    f(n, m) = \sum_{j = m}^5 f(n - 1, j)

几个初始条件也很容易写出来

-   `f(n, 5)` 说明没字母可选了，当然是0
-   `f(0, m)` 长度都是0了，当然是0
-   `f(1, m)` 说明只要放一个字母，那么有几个可选呢？有 `5 - m ` 个可选
"""

from typing import *

import functools


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @functools.lru_cache(None)
        def f(length: int, start: int) -> int:
            if start == 5 or length == 0:
                return 0
            elif length == 1:
                return 5 - start
            else:
                return sum(f(length - 1, j) for j in range(start, 5)) # 递推式照葫芦画瓢

        return f(n, 0)


s = Solution()
print(s.countVowelStrings(1))  # 5
print(s.countVowelStrings(2))  # 15
print(s.countVowelStrings(33))  # 66045
print(s.countVowelStrings(50))
