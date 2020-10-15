r"""
.. default-role:: math

在一个二维平面上，相机的位置是固定的、不能动，但是相机可以变换角度，相机的可视角度是 `a` 度。现在平面上有一些点，问相机的可视范围内最多可以看到多少个点。

哈哈，这个我最熟了，图形学也碰到过类似的问题，更何况这里还是二维的情况，比三维简单。

这个题目里某个点 `(x, y)` 在不在视野里，完全取决于点和相机的相对角度 `d` ，假设以相机的正右方为0度，上方为90度（也就是我们几何里学的那个右手系），假设相机的视野角度是 `f` ，那么当相机视野的最右边界在 `r` 的时候，相机视野的左边界是 `r + f` 。如果 `d \in [r, r + f]` ，那么就能看到这个点。

所以就先算出每个点相对相机的角度，从小到大排序。再试着把每个点都放在相机刚刚好能看到的地方，比如右边界上，然后用二分，找到最靠近相机左边界的那个点，这样整个视野范围内能看到的点就都有了。

那么怎么算出每个点相对相机的角度呢？很简单嘛， `\acos, \atan, \asin` 不都能用吗？问题是，假设有两个点 `(1, 1), (-1, -1)` ，它们用 `\atan` 算出来角度是一样的，都是45度……根本无法区分在哪个象限里。你说，可以加个判断嘛。

其实早就有内置的解决方法了，就是非常好用的 ``atan2(dy, dx)`` 函数，能给出 `(-pi, +pi]` 的结果，这样就能区分象限了。

还有个断层的问题啊，假设相机现在右边界在90度，结果相机是个超广角，角度达到了135度，那么左边界算出来就是225度，不在 `(-pi, +pi]` 的范围里了。好办好办，减去360就好了。

那视野里的点怎么算呢？分两部分算呗

::

    -178, -150, -90, 1, 2, ..., 178
                              |-------

    -178, -150, -90, 1, 2, ..., 178
    ----------|
"""

from typing import *

import math
import bisect


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        degrees = []
        always = 0 # 无论转到什么角度都能看到的点，当然就是和相机在同一个位置的点啦

        for x, y in points:
            if x == location[0] and y == location[1]: # 如果和相机的位置重合了
                always += 1 # 无论相机转到什么角度，都能看到这个点。单独拎出来计数吧，也不用放到degrees里面了，因为那样角度会变成未定义
            else:
                degrees.append(math.degrees(math.atan2(
                y - location[1], x - location[0]))) # 用atan2算出相对相机的角度，和平时学的右手系一致，+x是0，逆时针转动角度增加。atan2这个函数非常好用，能无损恢复出(-pi, pi]，这样就能区分四个象限了，不然的话用atan如果两个点一个在+x+y象限另一个在-x-y象限，atan值都是正数，根本无法区分

        degrees.sort() # 然后按相对相机的角度从小到大排序。但是要记住其实整个array是循环的，+pi过去就是-pi
        res = 0 # 除了那些和相机重合的点之外，视野里能看到的其他点最多有多少个

        for i, v in enumerate(degrees): # 对每个点，如果把相机的最右边的视野边界正好对准这个点，整个相机视野里面能容纳多少个点呢？
            # 要处理一下视野左边界的角度超过+pi和没超过+pi的情况
            if v + angle > 180: # 相机视野左边界跨越了断层
                index = bisect.bisect_right(degrees, v + angle - 360) # 比如现在左边界的角度是185度，超过了180度，所以要wrap回来，变成-175度，这时候视野里可以看到的点是degrees[i: ]和degrees[: index]
                res = max(res, len(degrees) - i + index) # degrees[i: ]里总共有len - i个点，degrees[: index]里总共有index个点
            else: # 左边界没有跨越边界
                index = bisect.bisect_right(degrees, v + angle) # 那就简单了，直接二分就可以了，视野里可以看到的点是degrees[i: index]
                res = max(res, index - i) # degrees[i: index]里总共有index - i个点

        return res + always # 加起来就好啦


s = Solution()
print(s.visiblePoints(points=[[2, 1], [2, 2], [
      3, 3]], angle=90, location=[1, 1]))  # 3
print(s.visiblePoints(points=[[2, 1], [2, 2], [
      3, 4], [1, 1]], angle=90, location=[1, 1]))  # 4
print(s.visiblePoints(points=[[0, 1], [2, 1]], angle=13, location=[1, 1]))  # 1
print(s.visiblePoints([[1, 1], [2, 2], [3, 3],
                       [4, 4], [1, 2], [2, 1]], 0, [1, 1]))  # 4
