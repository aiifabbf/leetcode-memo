"""
给直方图（而不是原数据），算出最小值、最大值、平均数、中位数、众数。

.. [#] 原来众数的英文是mode啊。

-   最小值

    就是直方图里最小的值非0的下标， :math:`O(n)` 能搞定。

-   最大值

    同理，直方图里最大的值非0的下标， :math:`O(n)` 能搞定。

-   平均数

    就是直方图的加权和再除以样本总数， :math:`O(n)` 能搞定。

-   中位数

    中位数感觉是最麻烦的一个。如果

    -   样本总个数是奇数，那么要找到第 ``n // 2`` 个数
    -   样本总个数是偶数，那么要找到第 ``n // 2`` 个数、第 ``n // 2 + 1`` 个数

-   众数

    直方图里的最大值， :math:`O(n)` 能搞定
"""

from typing import *

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        number = sum(count) # 样本总个数
        # minimum = min(filter(lambda v: count[v] != 0, range(256))) # 最小值
        minimum = min(filter(lambda v: v[1] != 0, enumerate(count)), key=lambda v: v[0])[0]
        # maximum = max(filter(lambda v: count[v] != 0, range(256))) # 最大值
        maximum = max(filter(lambda v: v[1] != 0, enumerate(count)), key=lambda v: v[0])[0]
        mean = sum(i * v for i, v in enumerate(count)) / number # 平均值
        # mode = max(range(256), key=lambda v: count[v]) # 众数
        mode = max(enumerate(count), key=lambda v: v[1])[0]

        if number % 2 != 0: # 样本总个数是一个奇数
            countDown = number // 2 # 找到第n // 2个数

            for i, v in enumerate(count):
                if v != 0:
                    if countDown - v <= 0: # 说明第n // 2个数在这一堆里
                        return list(map(float, [minimum, maximum, mean, i, mode]))
                    else: # 说明第n // 2个数在后面的堆里
                        countDown = countDown - v
        else: # 样本总个数是一个偶数
            leftCountDown = number // 2
            rightCountDown = number // 2 + 1 # 找到第n // 2和第n // 2 + 1个数

            for i, v in enumerate(count): # 先找第n // 2个数
                if v != 0:
                    if leftCountDown - v <= 0:
                        left = i
                        break
                    else:
                        leftCountDown = leftCountDown - v
            
            for i, v in enumerate(count): # 找第n // 2 + 1个数
                if v != 0:
                    if rightCountDown - v <= 0:
                        right = i
                        break
                    else:
                        rightCountDown = rightCountDown - v

            return list(map(float, [minimum, maximum, mean, (left + right) / 2, mode])) # 中位数是第n // 2个数和第n // 2 + 1个数的平均

# s = Solution()
# print(s.sampleStats(count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])) # [1, 3, 2.375, 2.5, 3]
# print(s.sampleStats(count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])) # [1, 4, 2.18182, 2, 1]