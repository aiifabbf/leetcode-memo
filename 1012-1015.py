"""
找到所有小于等于N的、含有重复数字的正整数。

比如给你100，然后结果是 ``[11, 22, 33, 44, 55, 66, 77, 88, 99, 100]``。

暴力搜索写起来很简单……

.. code:: python

    len([i for i in range(1, N + 1) if len(str(i)) != len(set(str(i)))])

但是肯定是过不了的……
"""

from typing import *

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        