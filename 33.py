"""
一个从小到大排好序的、严格递增的array偏移了几个元素，要你在 :math:`O(\ln n)` 复杂度里找到某个元素的下标。

实际上直接用Python的 ``.index()`` 也很快……不过既然要求 :math:`O(\ln n)` ，那就迎合一下吧。

我的思路是先用二分搜索找到断点的位置，也就是原array第一个元素的位置。但是首先要判断以下原array到底有没有切断过……如果不判断的话，会麻烦死的 [#]_ 。判断方法超级简单，只要判断现在的这个array的第一个元素和最后一个元素的大小关系就可以了，如果发现第一个元素比最后一个元素小，那直接不用寻找断点位置了，因为根本没断过，直接丢给二分搜索就好了。否则就一定断过。

这个条件是充分必要的，画一个图就可以验证出来：画一个横着的梯形，然后发现无论从哪里切一刀、把左半边平移到右半边去，都会发现新的这个图形的第一个元素比最后一个元素大。

这个问题画图真的能解决很多问题。

::
                -
            -
        -
    -
                            -
                        -
                    -

.. [#] 真的，我写了一下，充满了暴力美学，用了很多次 ``try...except`` block。恶心死我了。
"""

from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []: # 小心驶得万年船
            return -1

        left = 0
        right = len(nums)

        if nums[0] >= nums[-1]: # 先判断原array有没有断过

            while left < right: # 找到断点的下标
                middle = (left + right) // 2

                if middle - 1 >= 0: # 当心越界啊
                    if nums[middle - 1] > nums[middle]: # 发现断点的特征：按理说排好序的array里不可能出现前一个元素比后一个元素还大的情况的，这里出现了，说明这里断过
                        breakingPosition = middle # 而且middle正好就是原array第一个元素的下标
                        break
                else: # 越界了
                    breakingPosition = 0 # 那还是说明没断过
                    break

                if nums[middle] > nums[0]: # 发现middle处的这个数比第一个数大，这说明了middle在最小值的左侧、断点在middle的右边。同样可以从图上得出这个结论，因为原array是排好序的，所以断点左边的数都比第一个数大、断点右边的数都比第一个数小（因为最后一个元素又比第一个元素小）
                    left = middle + 1
                elif nums[middle] < nums[0]: # 说明middle在最小值的右侧、断点在middle的左边
                    right = middle

        else:
            breakingPosition = 0

        # 这时候就找到了分裂点middle，第middle个元素是原array里最大的元素，第middle + 1个元素是原array里最小的元素。下面开始分情况二分搜索。

        if breakingPosition == 0: # 原array根本没断过
            left = 0
            right = len(nums)
        else:
            if target >= nums[0]: # target值一定在断点的左边
                left = 0
                right = breakingPosition
            else: # target值一定在断点的右边
                left = breakingPosition
                right = len(nums)

        while left < right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            else:
                return middle

        return -1


# s = Solution()
# assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
# assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
# assert s.search([1, 3], 0) == -1
# assert s.search([], 5) == -1
# assert s.search([1, 2, 3, 4, 5], 6) == -1
# assert s.search([1, 2, 3, 4, 5, 6], 3) == 2
# assert s.search([3, 1], 3) == 0
# assert s.search([3, 1], 2) == -1
# assert s.search([2, 3, 4, 5, 1], 1) == 4
# assert s.search([2], 2) == 0
# assert s.search([2], 1) == -1