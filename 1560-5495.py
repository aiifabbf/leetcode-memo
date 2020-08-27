"""
.. default-role:: math

给一个循环圆盘，上面逆时针有 `1, 2, 3, ..., n` 一共 `n` 个刻度，再给一个路径，问经过最多次的刻度有哪些。

比如给

::

    1, 3, 1, 2

的意思是

::

    1 -> 2 -> 3 -> 4 -> 1 -> 2
    ^         ^         ^    ^

经过最多次的刻度是1和2。

很无聊，用个counter记录一下就好了。
"""

from typing import *

import collections


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        counter = collections.Counter()

        for i in range(1, len(rounds)):  # 记下[起点， 终点)，最后再补上最后一个终点，这样才不会重复统计
            start = rounds[i - 1]  # 起点
            end = rounds[i]  # 终点
            if end >= start:  # 没有绕圈，比如1 -> 2

                for j in range(start, end):
                    counter[j] += 1

            else:  # 绕圈了，比如3 -> 4 -> 1

                for j in range(start, n + 1):
                    counter[j] += 1

                for j in range(1, end):
                    counter[j] += 1

        counter[rounds[-1]] += 1  # 补上最后一个终点

        maxOccurrenceCount = max(counter.values())  # 最大频次

        # 挑出所有频次等于最大频次的刻度，还要从小到大排好序
        return sorted(k for k, v in counter.items() if v == maxOccurrenceCount)


s = Solution()
print(s.mostVisited(4, [1, 3, 1, 2]))
print(s.mostVisited(2, [2, 1, 2, 1, 2, 1, 2, 1, 2]))
print(s.mostVisited(7, [1, 3, 5, 7]))
