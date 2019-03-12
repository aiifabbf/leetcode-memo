# 有点像杂化轨道的感觉，要尽量远离其他元素使得总能量最小。

from typing import *

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = seats.index(1) # 第一个人的位置
        maxDistance = left # 坐第一个人的左边
        while left < len(seats):
            try:
                right = seats.index(1, left + 1) # 下一个人的位置，但有可能上一个人已经是最右边一个人了，所以加个try
                maxDistance = max(maxDistance, (right - left) // 2) # 坐上一个人和下一个人之间能量最小的位置
                left = right
            except: # 说明上一个已经是最右边一个人了
                maxDistance = max(maxDistance, len(seats) - 1 - left) # 坐在最右边一个人的右边
                break

        return maxDistance

s = Solution()
assert s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
assert s.maxDistToClosest([1, 0, 0, 0]) == 3
assert s.maxDistToClosest([0, 0, 1]) == 2