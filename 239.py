r"""
.. default-role:: math

给一个全是数字的array，长度为 `n` ，有一个长度为 `k` 的窗口在这个array上面从最左边开始往右滑动，每次取出这个窗口里的最大值。

比如给一个array

::

    1 3 -1 -3 5 3 6 7

长度为3的窗口在上面滑动、同时取窗口内最大值的结果是

::

    1 3 -1 -3 5 3 6 7
    ------            3
      -------         3
        -------       5
           ------     5
              ------  6
                ----- 7

所以结果是 ``3, 3, 5, 5, 6, 7`` 。

暴力做法就是不停地滑啊，从最左边到最右边总共能放进 `n - k + 1` 个长度为 `k` 的窗口，每次需要遍历一遍窗口内的 `k` 个数字才能得到当前窗口内的最大值，所以暴力做法的复杂度是 `O(k (n - k + 1))` 。当 `k = {n \over 2}` 的时候，复杂度阶数最高，是 `O(n^2)` 。

暴力做法是能过的……不过最好还是想一下有没有 `O(n)` 做法。

我能想到heap的做法，复杂度是 `O(n \ln n)` ，能过。heap里面不要只存一个数字，要连同数字出现的位置一起存，也就是存 ``(v, i)`` 。因为python的heap是最小heap，而我们要的是最大值，所以应该存值的倒数、连同位置，也就是存 ``(-v, i)`` 。

每次往右移动窗口一个单位之后，把当前窗口里最右边的数字的倒数连同下标一起放入到heap里面，然后不停地从heap里pop元素出来

-   如果下标在当前窗口范围内，就取这个结果，同时要把这个元素再重新放回heap
-   如果下标不在当前窗口范围内，就直接丢弃掉这个元素，继续pop
"""

from typing import *

import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        else:
            heap = [(- nums[i], i) for i in range(0, k)] # 初始窗口是nums[0: k]
            heapq.heapify(heap)
            res = [max(nums[0: k])] # 初始结果

            for i in range(1, len(nums) - k + 1): # 窗口从1开始移动，移动到n - k
                heapq.heappush(heap, (- nums[i - 1 + k], i - 1 + k)) # 把当前窗口最右边的元素放到heap里面

                while True: # 不停的pop heap，直到找到下标在当前窗口范围内的数字
                    negativeMaximum, index = heapq.heappop(heap)
                    maximum = - negativeMaximum
                    if index < i: # 发现这个数字在窗口外面
                        continue # 直接丢弃掉，继续pop
                    else: # 这个数字在窗口范围内
                        heapq.heappush(heap, (negativeMaximum, index)) # 记得放回heap
                        break # 停止while

                res.append(maximum)

            return res

# s = Solution()
# print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
# print(s.maxSlidingWindow([], 0))