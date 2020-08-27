"""
.. default-role:: math

给一个无限长的全0 array，给另一个array，每个数表示这一步把哪个0变成1，问全0 array里存在长度为 `m` 的连续1 substring（要连续）的最后一步是哪一步。

.. 好难讲清楚啊。

比如给 ``[3, 5, 1, 2, 4]`` ，表示

::

    3: 00000 -> 00100 ["1"]
         ^        ^

    5: 00100 -> 00101 ["1", "1"]
           ^        ^

    1: 00101 -> 10101 ["1", "1", "1"]
       ^        ^

    2: 10101 -> 11101 ["111", "1"]
        ^        ^

    4: 11101 -> 11111 ["11111"]
          ^        ^

最后一次出现长度为1的连续1 substring的步骤是第4步。第5步之后，就不存在长度是1的全1 substring了。

和128解法一样。搞两个hash map，一个hash map叫 ``lefts`` ，它key是左边界、value是右边界，另一个hash map叫 ``rights`` ，它的key是右边界、value是左边界。

第 `i` 个数从0变成1的时候，看一下 `i` 在不在 ``rights`` 里，如果在，说明左边存在一个区间 `[l, i)` 可以合并。

看一下 `i + 1` 在不在 ``lefts`` 里，如果在，说明右边存在一个区间 `[i + 1, r)` 可以合并。

再搞一个counter， ``counter[length] = count`` 表示现在有count个长度是length的区间。
"""

from typing import *

import collections


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        lefts = dict()  # lefts[left] = right表示之前见过一个[left, right)区间
        rights = dict()  # rights[right] = left表示之前见过一个[left, right)区间
        counter = collections.Counter()  # counter[length] = count表示至今有count个长度是length的区间
        res = -1

        for step, i in enumerate(arr):
            i = i - 1

            mergedLeft = i  # 合并后的区间左边界
            mergedRight = i + 1  # 合并后的区间的右边界
            # 如果不需要合并，那么区间是[i, i + 1)

            if 0 <= i - 1 < len(arr):
                if i in rights:  # 需要和左边紧邻的组合并
                    left = rights[i]
                    right = i
                    mergedLeft = left

                    # 既然要和左边紧邻的组，就先把左边的记录删掉
                    lefts.pop(left)
                    rights.pop(right)
                    counter[right - left] -= 1

            if 0 <= i + 1 < len(arr):
                if i + 1 in lefts:  # 需要和右边紧邻的组合并
                    left = i + 1
                    right = lefts[i + 1]
                    mergedRight = right

                    # 同理，删掉右边紧邻的组的记录
                    lefts.pop(left)
                    rights.pop(right)
                    counter[right - left] -= 1

            # 到这里，不管是合并了左边、右边、还是都没合并，总之形成了一个新的区间[mergedLeft, mergedRight)
            lefts[mergedLeft] = mergedRight
            rights[mergedRight] = mergedLeft
            counter[mergedRight - mergedLeft] += 1

            if m in counter and counter[m] != 0: # 如果至今还存在一个长度是m的区间
                res = step + 1

        return res


s = Solution()
print(s.findLatestStep([3, 5, 1, 2, 4], 1)) # 4
print(s.findLatestStep([3, 1, 5, 4, 2], 2)) # -1
print(s.findLatestStep([1], 1)) # 1
print(s.findLatestStep([2, 1], 2)) # 2
