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

还有更快的 `O(n)` 的做法，用单调递减队列做。

看了 <https://labuladong.gitbook.io/algo/shu-ju-jie-gou-xi-lie/dan-tiao-dui-lie> 终于知道单调非严格递减队列的写法了。和heap的做法差不多，只是用非严格单调递减queue取代heap。

具体怎么做呢？每次来一个新元素放到queue里，都要保证queue的单调递减性质。比如假设现在queue里是

::

    3, 2, 1

现在来了个4，首先它发现1比自己小，所以1被pop掉了。接着又发现2也比自己小，所以2也被pop掉了。最后发现3还是比自己小，3也被pop掉了。最后queue里就只剩下

::

    4

了。

因为queue是单调递减的，所以最开头的元素肯定是queue里面最大的元素。但是这个最开头的元素不一定是当前窗口里最大的元素，因为这个元素不一定在当前窗口范围内。

那么既然不在当前窗口范围内，它也不可能在之后的窗口里，所以遇到这种情况就直接扔掉，看下一个，总会遇到在当前窗口范围内的元素的。

这种做法正确的原因我觉得从直观上理解有两点

-   如果某个queue里的元素被后面新加进来的更大元素替代，那么这个元素就不再可能是当前窗口的最大值了，所以可以直接扔掉
-   如果某个queue里的元素已经不在当前窗口范围内了，那么这个元素更不可能在之后的窗口范围内，所以也可以直接扔掉

这两点保证了算法的正确。
"""

from typing import *

import heapq
import collections # 用链表更快

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if len(nums) == 0:
        #     return []
        # else:
        #     heap = [(- nums[i], i) for i in range(0, k)] # 初始窗口是nums[0: k]
        #     heapq.heapify(heap)
        #     res = [max(nums[0: k])] # 初始结果

        #     for i in range(1, len(nums) - k + 1): # 窗口从1开始移动，移动到n - k
        #         heapq.heappush(heap, (- nums[i - 1 + k], i - 1 + k)) # 把当前窗口最右边的元素放到heap里面

        #         while True: # 不停的pop heap，直到找到下标在当前窗口范围内的数字
        #             negativeMaximum, index = heapq.heappop(heap)
        #             maximum = - negativeMaximum
        #             if index < i: # 发现这个数字在窗口外面
        #                 continue # 直接丢弃掉，继续pop
        #             else: # 这个数字在窗口范围内
        #                 heapq.heappush(heap, (negativeMaximum, index)) # 记得放回heap
        #                 break # 停止while

        #         res.append(maximum)

        #     return res
        # 上面是heap写法，最直接，我能想到

        # 下面是单调递减queue写法，我想不到

        if len(nums) == 0:
            return 0
        else:
            queue = collections.deque() # queue里面存(array[i], i)。每次从最前面取出最大值的时候，都要检查一下这个最大值到底是不是当前窗口里的，所以一定要存i

            for i, v in enumerate(nums[: k]): # 初始窗口里元素下标范围是[0, k)

                while queue:
                    if queue[-1][0] < v:
                        queue.pop()
                    else:
                        break

                queue.append((v, i))

            res = [queue[0][0]] # 初始窗口里的最大值

            for i in range(1, len(nums) - k + 1): # 窗口左边界的范围是[1, n - k]
                v = nums[i + k - 1] # 新加的元素

                while queue: # 将要把新加的元素放到queue里，同时要维护queue单调递减的性质
                    if queue[-1][0] < v:
                        queue.pop()
                    else:
                        break

                queue.append((v, i + k - 1)) # 把新加的元素放进queue里

                while queue: # 从queue的前面取元素出来
                    if queue[0][1] >= i: # 如果第一个元素在窗口范围内
                        res.append(queue[0][0]) # 那么当前窗口的最大元素就是这个元素了
                        break
                    else: # 如果第一个元素不在窗口范围内
                        queue.popleft() # 扔掉

            return res

s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)) # 3, 3, 5, 5, 6, 7
print(s.maxSlidingWindow([], 0)) # []