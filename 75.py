"""
.. default-role:: math

给只含有 ``0, 1, 2`` 的array从小到大排序，不能用额外空间，要求 `O(n)` 时间。

超级经典的问题，外面叫 `荷兰国旗问题 <https://en.wikipedia.org/wiki/Dutch_national_flag_problem>` _ 。

和283非常像，但是比283难。283只需要把array里所有的 ``0`` 全部移动到array的最后方，这里是要排序。

不过想一下也很简单啊，可以归约到283。怎么做呢

1.  先把所有的 ``1`` 全部移动到array的最后方
2.  再把所有的 ``2`` 全部移动到array的最后方

不就好了？这是我认为最好的做法，又好理解又好写。缺点就是扫两遍。

也有扫一遍的做法。把水滴分成左半球和右半球，水滴移动的过程中，保持左半球里全都是 ``1`` 、右半球里全是 ``2`` 。其实挺难写的，需要考虑左半球或者右半球为空的情况，分别处理。
"""

from typing import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for v in [1, 2]: # 第一遍扫描先把所有的1移到后面；第二遍扫描再把所有的2移到后面
            left = 0 # 水滴的左边界
            right = 0 # 水滴的右边界

            while right < len(nums):
                if nums[right] == v: # 如果水滴右边第一个元素正好是1的话
                    right += 1 # 纳入到水滴里面来
                else: # 如果是其他的话
                    nums[left], nums[right] = nums[right], nums[left] # 交换一下，相当于水滴往前面移动了一格
                    left += 1
                    right += 1

            # 扫一遍的做法，看看就好了，我觉得理解起来简单，但是就是写起来特别烦
            # left = 0
            # middle = 0
            # right = 0

            # while right < len(nums):
            #     if nums[right] == 0:
            #         if left == right == middle:
            #             pass
            #         elif left == middle < right:
            #             nums[left], nums[right] = nums[right], nums[left]
            #         elif left < middle == right:
            #             nums[left], nums[right] = nums[right], nums[left]
            #         else: # left < middle < right
            #             nums[left], nums[middle], nums[right] = nums[right], nums[left], nums[middle]

            #         left += 1
            #         middle += 1
            #         right += 1
            #     elif nums[right] == 1:
            #         if left == right == middle:
            #             pass
            #         elif left == middle < right:
            #             nums[left], nums[right] = nums[right], nums[left]
            #         elif left < middle == right:
            #             pass
            #         else: # left < middle < right
            #             nums[middle], nums[right] = nums[right], nums[middle]

            #         middle += 1
            #         right += 1
            #     elif nums[right] == 2:
            #         right += 1