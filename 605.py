"""
给一个array，里面全是0或者1，现在要往这个array里填n个1，并且填完之后array中不能出现两个1相邻的情况，问你是否可能。

先考虑两个1之间最多可以插入多少个1。假设两个1的下标是i、j，找规律

::

    1 1             -> j - i = 1 -> 0
    1 _ 1           -> j - i = 2 -> 0
    1 _ _ 1         -> j - i = 3 -> 0
    1 _ _ _ 1       -> j - i = 4 -> 1
    1 _ _ _ _ 1     -> j - i = 5 -> 1
    1 _ _ _ _ _ 1   -> j - i = 6 -> 2
    ...

可以敏锐地（误）发现大概是和j - i的0.5倍有一个关系（但是1的时候又不是）。如果非要用表达式写出来，是一个分段函数 ``(j - i - 1 - 1) // 2 if i - j - 1 != 0 else 0`` 。

再来考虑左半边或者右半边没有的情况。找规律

::

    1               -> n = 0 -> 0
    _ 1             -> n = 1 -> 0
    _ _ 1           -> n = 2 -> 1
    _ _ _ 1         -> n = 3 -> 1
    _ _ _ _ 1       -> n = 4 -> 2
    ...

找到了，是非常规整的n整除2 ``n // 2`` 的形式。

右半边没边界的情况同理。

还有左半边、右半边都没有边界的情况也要考虑，毕竟题目也没说不会出现这种情况。找规律

::

                    -> n = 0 -> 0
    _               -> n = 1 -> 1
    _ _             -> n = 2 -> 1
    _ _ _           -> n = 3 -> 2
    _ _ _ _         -> n = 4 -> 2
    _ _ _ _ _       -> n = 5 -> 3
    ...

也是非常规整的 ``(n + 1) // 2``的形式
"""

from typing import *

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        try: # 考虑找不到1，也就是左右边界都不存在的情况
            onePosition = flowerbed.index(1)
        except:
            return (length + 1) // 2 >= n
        spaceLeft = onePosition # 左边的剩余空间
        capacity = spaceLeft // 2
        
        # for i, v in enumerate(flowerbed):
        #     if v == 1:
        #         # capacity += self.flowerCounterBetween(i - onePosition)
        #         capacity += (i - onePosition - 1) // 2
        #         onePosition = i
        #     # print(i, capacity)
        # 一改：用while好理解一点吧……虽然复杂度是一样的，都是扫描一遍。但是我怎么总是觉得自带的.index()要比我一个一个迭代快呢……
        while True:
            try:
                i = flowerbed.index(1, onePosition + 1) # 找到下一个1的位置
            except:
                break # 找不到就进入最后阶段
            # capacity += self.flowerCounterBetween(i - onePosition)
            capacity += (i - onePosition - 1 - 1) // 2 if i - onePosition - 1 != 0 else 0
            onePosition = i
            # print(i, capacity)
        
        # 下面开始处理右边界不存在的情况
        spaceLeft = length - onePosition - 1 # 右边的剩余空间
        capacity += spaceLeft // 2
        # print(capacity)
        return capacity >= n

    # def flowerCounterBetween(self, n): # 计算下标相差n的两个1之间可以插入多少个1
    #     if n <= 3:
    #         return 0
    #     else:
    #         return (n - 2) // 2
    # 可以用语句 (i - onePosition - 1 - 1) // 2 if i - onePosition - 1 != 0 else 0 少一个function call岂不是美滋滋。

s = Solution()
assert s.canPlaceFlowers([0], 1)
assert s.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
assert s.canPlaceFlowers([0, 0, 0, 0], 2)
assert s.canPlaceFlowers([1, 0], 1) == False
assert s.canPlaceFlowers([0, 0, 1, 0, 1], 1)
assert s.canPlaceFlowers([1, 0, 1, 0, 0, 1, 0], 1) == False