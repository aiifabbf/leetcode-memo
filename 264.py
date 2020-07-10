r"""
.. default-role:: math

给所有 `5^{a_3} 3^{a_2} 2^{a_1}` 从小到大排序，取出第 `n` 个数（下标从1开始），其中 `a_1, a_2, a_3 \in N` 。

暴力做法就是生成所有的 `5^{a_3} 3^{a_2} 2^{a_1}` 再排序，取出第 `n` 个数就好了。当然有无限多个数字，只要生成最大整数之内的就可以了。

研究一下递推式，发现如果已经得到了前 `k` 个数，第 `k + 1` 个数可以用

.. math::

    u_{k + 1} = \min\left\{\begin{aligned}
        && 2 u_1, 2 u_2, ..., 2 u_k \\
        && 3 u_1, 3 u_2, ..., 3 u_k \\
        && 5 u_1, 5 u_2, ..., 5 u_k
    \end{aligned}\right\}

得到。可以用一个heap来存这个表格，这样每次pop出来的都是最小的，复杂度降低到了 `O(n \ln n)` 。

但是仍然有一个问题：表格里面会出现很多重复的数字，如果pop出很多重复的数字，就很浪费时间。所以我这边伴随heap，还弄了一个set，set里的内容和heap完全相同。需要把数字插入到heap之前，先检查set里有没有这个数字，如果没有，再插入到heap里，同时更新set。

虽然是费点内存。
"""

from typing import *

import heapq

class Solution:
    # def nthUglyNumber(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     else:
    #         res = [1] # 存u_1, u_2, ..., u_n
    #         usable = [] # 存表格
    #         heapq.heapify(usable) # 用heap，这样每次pop出来都是最小的
    #         setUsable = set() # 表格里面会有很多重复的数，用set保证插入到heap里面的数都是没有重复的

    #         while len(res) != n: # 直到u_n

    #             for v in [2, 3, 5]: # 生成2 u_k, 3 u_k, 5 u_k并且插入到heap中
    #                 if v * res[-1] not in setUsable: # 当然要保证heap里没有这个数
    #                     setUsable.add(v * res[-1])
    #                     heapq.heappush(usable, v * res[-1])

    #             temp = heapq.heappop(usable) # 从表格中取出最小的那个数
    #             res.append(temp) # 取出来的那个数就是u_{k+1}

    #         return res[-1] # u_n是最后一个数字

    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        usable = [2, 3, 5]
        heapq.heapify(usable)
        seen = {2, 3, 5}
        res = [1]

        for i in range(n - 1):
            node = heapq.heappop(usable)
            res.append(node)

            for j in [2, 3, 5]:
                if node * j not in seen:
                    seen.add(node * j)
                    heapq.heappush(usable, node * j)

        return res[-1]

# s = Solution()
# print(s.nthUglyNumber(10)) # 12
# print(s.nthUglyNumber(263)) # 48600