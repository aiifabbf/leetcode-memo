"""
.. default-role:: math

电影院有 `n` 排座位，每排都有10个座位，呈 ``3, 4, 3`` 分布，中间是过道。有一些座位事先被预定了。现在问总共最多能容纳多少4人家庭来看电影。4人家庭里的4个人必须坐在同一排、而且位置下标要连续，此外如果中间隔了过道的话，必须保证过道左边2个人、右边2个人。

座位排布大概是这样的

::

    1 2 3 || 4 5 6 7 || 8 9 10

``||`` 表示过道。

看上去挺吓人的，不过仔细想一下就两种大的情况

-   这排没人预定

    那好办，直接坐2个4人家庭。像这样

    ::

        _ x x || x x y y || y y _

-   这排有人预定

    这里就要看情况了。我们的目标是要尽可能多安排家庭坐下，所以分别看看左边和右边能不能坐下。也就是说 ``2, 3, 4, 5`` 是否空着、 ``6, 7, 8, 9`` 是否空着。

    如果 ``2, 3, 4, 5, 6, 7, 8, 9`` 都空着，那么等效于没人预定，直接坐2个家庭。类似这样

    ::

        ? x x || x x y y || y y ?

    如果 ``2, 3, 4, 5`` 有某个被预定了，但是 ``6, 7, 8, 9`` 空着，那么只能坐下1个家庭。

    ::

        ? ? ? || ? ? y y || y y ?

    如果 ``2, 3, 4, 5`` 全空，但是 ``6, 7, 8, 9`` 有某个被预定了，那么还是只能坐下1个家庭。

    ::

        ? x x || x x ? ? || ? ? ?

    如果 ``2, 3, 4, 5`` 有被预定的、 ``6, 7, 8, 9`` 也有被预定的，那么最后看一下最中间的4个座位有没有空，也就是 ``4, 5, 6, 7`` 是不是 **全空** ，如果全空，那么这里可以坐下1个家庭。如果这个也有被预定了的，那没办法了，这排没法安排4人家庭了。

    ::

        ? ? ? || x x x x || ? ? ?
"""

from typing import *


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = dict() # key是排号，value是一个集合，包含了这排所有被预定的座位的列号

        for rowIndex, columnIndex in reservedSeats:
            if rowIndex in reserved:
                reserved[rowIndex].add(columnIndex)
            else:
                reserved[rowIndex] = {columnIndex}

        res = (n - len(reserved)) * 2 # 空的排可以直接坐下2个家庭

        for rowIndex, reservedThisRow in reserved.items():
            if any(v in reservedThisRow for v in [2, 3, 4, 5]): # 2, 3, 4, 5是否全空
                left = False
            else:
                left = True

            if any(v in reservedThisRow for v in [6, 7, 8, 9]): # 6, 7, 8, 9是否全空
                right = False
            else:
                right = True

            if any(v in reservedThisRow for v in [4, 5, 6, 7]): # 中间能不能坐下
                middle = False
            else:
                middle = True

            if left and right: # 如果两边都能坐
                res += 2 # 当然安排两个家庭
            elif left and not right: # 只有左边能坐
                res += 1 # 安排一个家庭
            elif not left and right: # 只有右边能坐
                res += 1 # 安排一个家庭
            elif middle: # 只要中间能坐
                res += 1 # 安排一个家庭
            # 全不能坐，没办法了，这排只能跳过

        return res


s = Solution()
print(s.maxNumberOfFamilies(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]))
print(s.maxNumberOfFamilies(n=2, reservedSeats=[[2, 1], [1, 8], [2, 6]]))
print(s.maxNumberOfFamilies(n=4, reservedSeats=[[4, 3], [1, 4], [4, 6], [1, 7]]))
