"""
.. default-role:: math

给两个都是左闭右闭区间的数组，代表两个人的空闲时间，再给一个开会时长，问哪段时间可以安排这两个人一起开个会？

比如给第一个人的空闲时间

::

    [10, 50], [60, 120], [140, 210]

和第二个人的空闲时间

::

    [0, 15], [60, 70]

要找一段长度是9分钟的空闲时间，可以找

::

    [60, 69)

这个区间等价于

::

    [60, 68]

这个区间是最早的、两个人可以凑到一起开会的时间。

这个题面有不清晰的地方：说是说要找长度为8分钟的区间，但是区间 `[60, 68]` 里明明是9分钟。所以我这里只能理解成，实际上要找的是题目里给的长度+1的左闭右开区间，返回的时候要返回这个左闭右开区间的左闭右闭形式。

看题目数据规模应该是要找到一个 `O(n)` 复杂度的算法。

先考虑一下，假设当前有两个空闲区间，这两个空闲区间需要满足什么条件，才能凑出时间来开会呢？

首先这两个区间的起始时间会有3种情况

-   第一个区间的起始时间大于第二个区间的起始时间
-   第一个区间的起始时间等于第二个区间的起始时间
-   第一个区间的起始时间小于第二个区间的起始时间

先来看第一种情况下，这两个空闲区间需要满足什么条件

::

        |-----|
    |-------|

看了这个图很明显了，第一个区间的起始时间加上会议时间要小于等于第二个区间的终止时间。这样想的话就会漏掉这种情况

::

        |-|
    |-------|

所以能凑出时间开会需要两个条件

-   第一个区间的起始时间加上会议时间要小于等于第二个区间的终止时间
-   第一个区间的起始时间加上会议时间要小于等于第一个区间的终止时间

那如果某个条件不满足呢？如果第一个区间的起始时间加上会议时间大于第二个区间的终止时间的话，那么第一个区间仍然有可能容纳会议，但是第二个区间无论如何都不可能容纳得下会议了。所以这时候应该看第二个区间后面的空闲区间了，也就是比较第一个区间和第二个区间紧接着的后面一个空闲区间。就像这样

::

        |-----|
    |------||-----|

如果第二个条件不满足，也就是如果第一个区间的起始时间加上会议时间大于第一个区间的终止时间的话，那么第一个区间无论如何都不可能容纳下会议。所以这时候应该直接看第一个区间后面紧接着的空闲区间了，也就是说，下一轮应该比较第一个区间紧接着的后面一个区间、和第二个区间。就像这样

::

        |-||----|
    |-------|
"""

from typing import *

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        duration += 1 # 实际上是要duration+1分钟的区间
        slots1 = sorted(slots1, key=lambda v: v[0]) # 按起始时间从小到大排序
        slots2 = sorted(slots2, key=lambda v: v[0]) # 按起始时间从小到大排序

        intervalIndex1 = 0 # 第一个人的当前区间
        intervalIndex2 = 0 # 第二个人的当前区间

        while intervalIndex1 < len(slots1) and intervalIndex2 < len(slots2):
            interval1 = slots1[intervalIndex1]
            interval1[1] += 1 # 把左闭右闭区间变成左闭右开区间
            interval2 = slots2[intervalIndex2]
            interval2[1] += 1 # 把左闭右闭区间变成左闭右开区间
            # 把左闭右闭区间变成左闭右开区间有一个好处是，右边界减去左边界就直接是区间的长度了，不用再加1或者减1那么麻烦了

            # 先比较两个人当前空闲区间的起始时间的大小关系，只会有三种情况
            if interval1[0] > interval2[0]: # 第一个人的当前区间的起始时间在第二个人的当前区间的起始时间后面
                if interval1[0] + duration <= interval2[1] and interval1[0] + duration <= interval1[1]: # 正好可以凑个时间
                    return [interval1[0], interval1[0] + duration - 1] # 返回这段时间，注意要把左闭右闭区间转换成左闭右开区间
                elif interval1[0] + duration > interval1[1]: # 第一个人的当前区间不够长
                    intervalIndex1 += 1 # 那没办法了，只能继续往后看第一个人的下一个空闲区间
                else: # 第二个人的当前区间不够长
                    intervalIndex2 += 1 # 往后看第二个人的下一个空闲区间
            elif interval1[0] < interval2[0]: # 第二个人的当前区间的起始时间在第一个人的当前区间的起始时间后面
                if interval2[0] + duration <= interval1[1] and interval2[0] + duration <= interval2[1]: # 正好可以凑个时间
                    return [interval2[0], interval2[0] + duration - 1]
                elif interval2[0] + duration > interval2[1]:
                    intervalIndex2 += 1
                else:
                    intervalIndex1 += 1
            else: # 第一个人的当前区间和第二个人的当前区间的起始时间相同
                if interval1[0] + duration <= interval1[1] and interval2[0] + duration <= interval2[1]: # 可以正好凑一个时间
                    return [interval1[0], interval1[0] + duration - 1]
                elif interval1[0] + duration > interval1[1]: # 第一个人的当前区间不够长
                    intervalIndex1 += 1 # 往后看第一个人的下一个空闲区间
                else: # 第二个人的当前区间不够长
                    intervalIndex2 += 1 # 往后看第二个人的下一个空闲区间

        return [] # 看完了第一个人的所有空闲时间或者第二个人的所有空闲时间之后都没有能够找到两个人都有空的足够长的时间区间来凑一起开会，所以这两个人没法凑到一起开会

s = Solution()
print(s.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8)) # [60, 68]
print(s.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12)) # []
print(s.minAvailableDuration([[0, 2]], [[1, 3]], 1)) # [1, 2]
print(s.minAvailableDuration([[0, 2]], [[1, 3]], 2)) # []