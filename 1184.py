"""
.. default-role:: math

有 `n` 个公交车站 `0, 2, 3, ..., n - 1` 在一个环上（也就是第 `n - 1` 个车站后面紧接着第0个公交站），第 `i` 个公交站和第 `i + 1` 个公交站之间的距离是 ``distance[i]`` ，第 `n - 1` 个公交站和第0个公交站之间的距离是 ``distance[n - 1]`` 。给一个起点 ``start`` 和一个终点 ``destination`` ，从起点的第 ``start`` 个车站走到终点的第 ``destination`` 个车站的最短距离是多少？

首先要发现一件事情，就是从第 ``start`` 个车站走到第 ``destination`` 个车站在任何情况下都是有两条路

-   可以从第 ``start`` 个车站往左走（也就是往index小的方向走），到达第 ``destination`` 个车站
-   可以从第 ``start`` 个车站往右走（也就是往index大的方向走），到达第 ``destination`` 个车站

这两条路的距离之间是有关系的。假设走一整圈，经过所有车站、回到最初出发的出站，走过的距离是 `L` ，从第 ``start`` 个车站出发往右（index增大的方向）走、到达第 ``destination`` 个车站经过的距离是 `a` , 那么从第 ``start`` 个车站出发往左（index减小的方向）走、到达第 ``destination`` 个车站经过的距离是 `b` ，那么一定有 `a + b = L` 。所以算出 `a` 就能自动算出 `b` 。

那么现在问题就是，算 `a` 还是算 `b` 比较容易呢。要看 ``start`` 和 ``destination`` 的大小关系

-   如果 ``destination > start`` ，也就是说终点在起点的右边（index增大的方向），那么算 `a` 比较好算，直接就是 ``sum(distance[start: destination])`` ， `b` 就用 `L - a` 算出来。
-   如果是 ``destination < start`` ，终点在起点的左边（index减小的方向），那么 `b` 比较好算，直接就是 ``sum(distance[destination: start])`` ， `a` 通过 `L - b` 算出来。
"""

from typing import *

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        circularDistance = sum(distance) # 绕一圈走过的路径长度
        if destination > start: # 如果终点在起点的“后面”
            a = sum(distance[start: destination]) # a比较好算
            return min(a, circularDistance - a) # 取顺时针方向和逆时针方向中的最小值
        else: # 终点在起点的“前面”
            b = sum(distance[destination: start]) # b比较好算
            return min(b, circularDistance - b) # 还是取两个方向的最小值

# s = Solution()
# print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 1)) # 1
# print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 2)) # 3
# print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 3)) # 4