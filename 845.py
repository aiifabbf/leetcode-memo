"""
找到一个array里 **山型** 的最长的substring（要连续）的长度。

所谓山型就是先严格增、后严格减。即在长度为m（m至少为3）的substring中，存在一个 :math:`0 < i < m - 1` 使得

.. math::

    b_0 < b_1 < \cdots < b_{i - 1} < b_i > b_{i + 1} > \cdots > b_{m - 1}
"""

from typing import *

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        