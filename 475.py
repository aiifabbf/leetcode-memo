r"""
.. default-role:: math

有一些房屋和一些炉子，炉子的加热半径最小是多少，才能使得所有房屋都能被加热到？

假设房屋的位置是 `\{a_k\}` ，炉子的位置是 `\{b_k\}` ，炉子的加热半径是 `r` ，那么就是要找到一个最小的 `r` ，使得

.. math::

    \forall k, \exists l: \qquad a_k \in [b_l - r, b_l + r]

所以思路是给每个房屋找到离这个房屋最近的炉子，得到房屋离最近的炉子的距离，然后取这个距离的最大值（这样才能保证每个房屋都能被覆盖到）。也就是求

.. math::

    \max_k \{\min_i \{|a_k - b_i|\}\}

假设总共有 `m` 个炉子、 `n` 个房子，暴力做法的复杂度是 `O(nm)` ，按照题目的数据规模要求应该是过不了的，需要想办法优化。

我能想到的就是给炉子的位置排序，然后以房子的位置为目标、在炉子的位置array里二分搜索。给炉子排序的复杂度是 `O(m \ln m)` ，每次搜索的复杂度是 `O(\ln m)` ，需要做 `n` 次搜索，所以搜索的复杂度是 `O(n \ln m)` 。所以总的复杂度是 `O((n + m) \ln m)` 。
"""

from typing import *

import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = sorted(heaters) # 给炉子的位置排序，这样才能做二分搜索
        heaterSet = set(heaters)
        res = 0

        for house in houses:
            if house in heaterSet: # 房子的位置上正好有炉子
                minimumRadiusToMakeThisHouseWarm = 0 # 半径直接是0
            else: # 房子的位置上没有炉子，必须靠左右两边的炉子来取暖
                nearestHeater = bisect.bisect(heaters, house)
                if nearestHeater == len(heaters): # 右边没有炉子
                    minimumRadiusToMakeThisHouseWarm = house - heaters[nearestHeater - 1] # 那么需要左边最近的炉子能覆盖到这个房子
                elif nearestHeater == 0: # 左边没有炉子
                    minimumRadiusToMakeThisHouseWarm = heaters[nearestHeater] - house # 需要右边最近的炉子能覆盖到这个房子
                else: # 两边都有炉子
                    minimumRadiusToMakeThisHouseWarm = min(house - heaters[nearestHeater - 1], heaters[nearestHeater] - house) # 二分搜索只能确定这个房子在这两个炉子之间，不能确定左边的炉子离房子更近还是右边的炉子离房子更近，所以两边都看一下，取最近的就好了
            res = max(res, minimumRadiusToMakeThisHouseWarm)

        return res

# s = Solution()
# print(s.findRadius([1, 2, 3], [2])) # 1
# print(s.findRadius([1, 2, 3, 4], [1, 4])) # 1