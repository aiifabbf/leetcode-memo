"""
给一个permutation，写出按字典顺序排列的这个permutation的下一个permutation。

比如 ``1, 2, 3`` 总共可以有6个permutation，按字典顺序从小到大排列是

::

    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1

给 ``[2, 1, 3]`` ，那么下一个permutation是 ``[2, 3, 1]`` 。

这个实在是完全没法想出来的，因为给你10个数手写你也写不出来。所以就直接看答案了。答案说按照下面的步骤做一定能做出来

1.  从后往前找是否存在一个 ``i`` 使得 ``a[i] < a[i + 1]`` ，如果不存在，说明array本来就是递减的了，因此是最大的permutation了，直接返回array的倒序，也就是第一个、最小的那个permutation。
2.  如果存在，从 ``a[i + 1: ]`` 里找到比 ``a[i]`` 大的最小的数。可能不止有一个 [#]_ ，这时候取下标最大的、也就是位置最靠右的那个，记为 ``a[j]``。

3.  交换 ``a[i], a[j]``。
4.  把 ``a[i + 1: ]`` 颠倒一下。

比如 ``[2, 3, 1, 3, 3]``

1.  从后往前找 ``a[i] < a[i + 1]`` ，发现 ``a[2] < a[3]``
2.  在 ``a[2 + 1: ]`` 也就是 ``[3, 3]`` 里面找比 ``1`` 大的最小的数，发现是3，可是有两个3，这时候就应该取靠右的 ``3`` 也就是 ``a[4]`` ，交换 ``a[2]`` 和 ``a[4]`` ，array变成 ``[2, 3, 3, 3, 1]``
3.  颠倒 ``a[2 + 1: ]`` 也就是 ``[3, 1]`` ，变成 ``[1, 3]`` 。此时array变成 ``[2, 3, 3, 1, 3]``

.. [#] `答案 <https://leetcode.com/problems/next-permutation/solution/>`_ 没有提到不止有一个 ``a[j]`` 的情况，只说了"just larger than itself"。
"""

from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(0, len(nums) - 1)): # 从后往前找第一个a[i] < a[i + 1]
            if nums[i] < nums[i + 1]: # 第一个找到的a[i] < a[i + 1]
                smallestNumberGreaterThanThisPosition = min(range(i + 1, len(nums)), key=lambda v: (nums[v], -v) if nums[v] > nums[i] else (float("inf"), 0)) # 首先需要这个数a[j]是a[i+1:]中比a[i]大的最小的数，其次是需要j尽可能大。所以这用(nums[v], -v)作为key，表示先比较大小（当然这里还用了inf来过滤掉小于等于a[i]的数），如果大小相等，再比较下标的倒数，表示越靠右越好
                nums[i], nums[smallestNumberGreaterThanThisPosition] = nums[smallestNumberGreaterThanThisPosition], nums[i] # 交换a[i], a[j]
                nums[i + 1: ] = nums[i + 1:][:: -1] # 颠倒a[i + 1: ]
                return
        else: # 没有找到一个a[i] < a[i + 1]
            nums[:] = nums[:: -1] # 直接颠倒整个array
            return

# s = Solution()

# a = [1, 2, 3]
# s.nextPermutation(a)
# print(a) # 1 3 2

# a = [3, 2, 1]
# s.nextPermutation(a)
# print(a) # 1 2 3

# a = [1, 1, 5]
# s.nextPermutation(a)
# print(a) # 1 5 1

# a = [2,3,1,3,3]
# s.nextPermutation(a)
# print(a) # 2 3 3 1 3