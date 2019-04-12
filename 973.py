"""
离原点最近的K个点

我不懂这个题为什么会是medium……
"""

from typing import *

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[: K]