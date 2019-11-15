r"""
.. default-role:: math

给一个字符串，从这个字符串里挑字符，每个字符只能用一次，最多能组成多少次 ``balloon`` 这个单词。

用 ``Counter`` ，很简单。先统计 ``balloon`` 这个单词里每个字符出现的次数，再统计给的字符串里每个字符出现的次数。 ``balloon`` 这个单词里，

-   ``b`` 出现了1次
-   ``a`` 出现了1次
-   ``l`` 出现了2次
-   ``o`` 出现了2次
-   ``n`` 出现了1次

所以我们到第二个直方图里看这5个字符出现了多少次，

-   假设 ``b`` 出现了 `b` 次
-   假设 ``a`` 出现了 `a` 次
-   假设 ``l`` 出现了 `l` 次
-   假设 ``o`` 出现了 `o` 次
-   假设 ``n`` 出现了 `n` 次

每个次数分别除以 ``balloon`` 里对应字符出现的次数，取最小值

.. math::

    \min\left\{{b \over 1}, {a \over 1}, {l \over 2}, {o \over 2}, {n \over 1}\right\}

就是答案了。

举个例子，比如 ``ballooon`` ，虽然 ``o`` 出现了3次，但是其他字符都只能恰好凑一整个 ``balloon`` ，所以答案只能是1。即使 ``o`` 出现了100次都没有用，只能取那个最小的倍数（有点短板原理的感觉？）
"""

from typing import *

import collections

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        templateCounter = collections.Counter("balloon")
        counter = collections.Counter(text)
        return min(map(lambda k: counter[k] // templateCounter[k], templateCounter))

# s = Solution()
# print(s.maxNumberOfBalloons("nlaebolko")) # 1
# print(s.maxNumberOfBalloons("loonbalxballpoon")) # 2
# print(s.maxNumberOfBalloons("leetcode")) # 0