"""
.. default-role:: math

给个有向图，最少从多少个起点开始才能遍历完图上的每个节点？

比如这个图

::

    0 -> 1
    |
    v
    2 -> 5
    ^
    |
    4
    ^
    |
    3

从 ``0`` 开始，可以遍历 ``0, 1, 2, 5`` ，从 ``3`` 开始可以遍历 ``3, 4, 2, 5`` ，所以只需要从2个节点开始就可以遍历完图上的所有节点。

观察一下，会发现两件事情

-   没有入边的节点只能作为起点，不然无论如何都不可能通过别的节点遍历到它们
-   任何一个节点只要有一条入边，就可以从上游遍历到这个节点

所以这道题就是数一下图上有多少个入度是0的节点……

.. 突然就想到拓扑排序的第一步。
"""

from typing import *

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # outs = dict() # 不需要用到出边图
        ins = dict()

        for a, b in edges:
            # if a not in outs:
            #     outs[a] = set()
            # outs[a].add(b)
            if b not in ins:
                ins[b] = set()
            ins[b].add(a)

        return [v for v in range(n) if v not in ins]

s = Solution()
print(s.findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]])) # [0, 3]
print(s.findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]])) # [0, 2, 3]