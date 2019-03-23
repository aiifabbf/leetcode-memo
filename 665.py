"""
能否最多只修改array中的一个元素，使得array变成递增 [#]_ 数列。

.. [#] 题目里是non-decreasing，给的定义是

    .. math::

        \forall 0 \leq i < j \leq n - 1, \qquad a_i \leq a_j

我的思路是从左往右依次、一下子考虑相邻的三个元素。 [#]_

.. [#] 可是为什么是三个元素？因为1个显然不够，我开始以为2个就够了，直到遇到了 ``[3, 4, 2, 3]`` 这个case。

相邻的三个元素之间的大小关系，粗看好像是27种，但是其中有很多种都是重复的。

::

    1 1 1
    1 1 2
    1 1 3 = 1 1 2
    1 2 1
    1 2 2
    1 2 3
    1 3 1 == 1 2 1
    1 3 2
    1 3 3 == 1 2 2
    2 1 1
    2 1 2
    2 1 3
    2 2 1
    2 2 2 = 1 1 1
    2 2 3 = 1 1 2
    2 3 1
    2 3 2 = 1 2 1
    2 3 3 = 1 2 2
    3 1 1 = 2 1 1
    3 1 2
    3 1 3 = 2 1 2
    3 2 1
    3 2 2 = 2 1 1
    3 2 3 = 2 1 2
    3 3 1 = 2 2 1
    3 3 2 = 2 2 1
    3 3 3 = 1 1 1

把需要考虑的情况单独列出来分析

-   ``1 1 1`` 三个一样大。没问题
-   ``1 1 2`` 一二一样大、三大一点。没问题
-   ``1 2 1`` 一三一样大、二大一点。有问题，可以通过一次调整解决，比如调小第二个或者调大第三个
-   ``1 2 2`` 二三一样大、一小一点。没问题
-   ``1 2 3`` 一二三依次升高。没问题
-   ``1 3 2`` 没规律。有问题，可以通过一次调整解决，比如调小第二个或者调大第三个
-   ``2 1 1`` 二三一样大、一大一点。有问题，可以通过一次调整解决，只能调小第一个
-   ``2 1 2`` 一三一样大、二小一点。有问题，可以通过一次调整解决，只能调大第二个
-   ``2 1 3`` 没规律。有问题，可以通过一次调整解决，可以调小第一个或者调大第二个
-   ``2 2 1`` 一二一样大、三小一点。有问题，可以通过一次调整解决，只能调大第三个
-   ``2 3 1`` 没规律。有问题，可以通过一次调整解决，只能调大第三个
-   ``3 1 2`` 没规律。有问题，可以通过一次调整解决，只能调小第一个
-   ``3 2 1`` 递减。有问题，并且没法通过一次调整解决

遇到有两种调整方案的情况，尽量选择调整序号小的元素，这样对后面的判断影响小。
"""

from typing import *

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
            return True
        else:
            abnormalCount = 0

            for i in range(1, len(nums) - 1):
                if nums[i - 1] > nums[i] > nums[i + 1]: # 321
                    return False
                elif nums[i] > nums[i - 1] == nums[i + 1]: # 121
                    nums[i] = nums[i + 1]
                    abnormalCount += 1
                elif nums[i - 1] < nums[i + 1] < nums[i]: # 132
                    nums[i] = nums[i - 1]
                    abnormalCount += 1
                elif nums[i - 1] > nums[i] == nums[i + 1]: # 211
                    nums[i - 1] = nums[i]
                    abnormalCount += 1
                elif nums[i] < nums[i - 1] == nums[i + 1]: # 212
                    nums[i] = nums[i - 1]
                    abnormalCount += 1
                elif nums[i + 1] > nums[i - 1] > nums[i]: # 213
                    nums[i - 1] = nums[i]
                    abnormalCount += 1
                elif nums[i - 1] == nums[i] > nums[i + 1]: # 221
                    nums[i + 1] = nums[i]
                    abnormalCount += 1
                elif nums[i + 1] < nums[i - 1] < nums[i]: # 231
                    nums[i + 1] = nums[i]
                    abnormalCount += 1
                elif nums[i] < nums[i + 1] < nums[i - 1]: # 312
                    nums[i - 1] = nums[i]
                    abnormalCount += 1
                else:
                    pass

            return abnormalCount <= 1