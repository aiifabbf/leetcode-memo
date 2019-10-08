"""
.. default-role:: math

给一个array， ``array[i]`` 表示第 `i` 张牌的位置。往左或者往右2格移动一张牌的花费是0，往左或者往右1格移动一张牌的花费是1。问最少需要多少花费，所有的牌才能凑到一堆上。

听起来很难实际上非常简单。首先因为把一张牌往左或者往右移动2格是免费的，所以尽管移动就好了，可以把

-   所有的奇数位置的牌全部免费地、2格2格地移动到位置1
-   所有的偶数位置的牌全部免费地、2格2格地移动到位置0

然后我们看位置1的牌多、还是位置0的牌多就好了，把牌少的那一堆花钱移动到牌多的那一堆。
"""

from typing import *

import collections

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        counter = collections.Counter(chips) # 统计每个位置上有多少张牌
        odds = 0 # 奇数位置上的牌的个数
        evens = 0 # 偶数位置上的牌的个数

        for k, v in counter.items():
            if k % 2 == 0:
                evens += v
            else:
                odds += v

        return min(evens, odds) # 把牌少的牌堆全部移动到牌多的那一堆，可以做到花费最少

# s = Solution()
# print(s.minCostToMoveChips([1, 2, 3])) # 1
# print(s.minCostToMoveChips([2, 2, 2, 3, 3])) # 2