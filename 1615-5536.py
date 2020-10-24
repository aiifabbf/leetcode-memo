"""
.. default-role:: math

给个无向无权图，定义 `r(a, b)` 表示端点是 `a` 或者 `b` 的边的集合，问整张图里面 `|r(a, b)|` 的最大值是多少。

.. 想到了 `vertex cover问题 <https://en.wikipedia.org/wiki/Vertex_cover>`_ 。

比如给个图

::

    0 - 1 - 2
      \ |
        3

那么 `r(0, 1) = \{(0, 1), (1, 2), (1, 3), (0, 3)\}` ，所以 `|r(0, 1)| = 4` 。

输入规模暗示暴力做就好了。对每一对 `(a, b)` 都去算一下 `r(a, b)` 。

有空再想想有没有高效做法……
"""

from typing import *


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = {} # 遇事不决，把图转换成adjacency set的表示形式，用着舒心

        for i in range(n):
            graph[i] = set()

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        res = 0

        for a in graph.keys():
            for b in graph.keys():
                roads = set() # r(a, b)

                # 记下端点是a的所有的边
                for target in graph[a]:
                    roads.add(tuple(sorted([a, target]))) # 为了防止重复计算，表示边的时候，序号小的端点放在前面，写成(0, 1)而不是(1, 0)

                # 记下端点是b的所有的边
                for target in graph[b]:
                    roads.add(tuple(sorted([b, target])))

                res = max(res, len(roads))


        return res