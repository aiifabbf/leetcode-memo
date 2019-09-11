"""
实现排序

当然是用我最喜欢的merge sort啦。
"""

from typing import *

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: # 空array
            return []
        elif len(nums) == 1: # 只有一个元素的array
            return nums
        elif len(nums) == 2: # 只有两个元素的array
            return [min(nums), max(nums)]
        else: # 元素数量大于2的，拆成数量尽量均匀的前半部分和后半部分
            left = self.sortArray(nums[: len(nums) // 2]) # 前半部分排序一下
            right = self.sortArray(nums[len(nums) // 2: ]) # 后半部分排序一下
            res = [] # 存放merge的结果

            while len(left) != 0 and len(right) != 0: # 开始merge
                if left[0] > right[0]: # 比较最前面两个元素的大小，把小的那个放到结果array的最后
                    res.append(right.pop(0))
                else:
                    res.append(left.pop(0))

            if left: # right中的元素取完了
                res.extend(left) # 直接把前半部分剩下的元素放到结果的后面
            else: # left中的元素取完了
                res.extend(right) # 直接把后半部分剩下的元素放到结果的后面

            return res

# s = Solution()
# print(s.sortArray([5, 2, 3, 1]))
# print(s.sortArray([5, 1, 1, 2, 0, 0]))