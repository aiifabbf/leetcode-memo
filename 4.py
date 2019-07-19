"""
.. default-role:: math

给两个从小到大排好序的array，问这两个array合并起来之后，中位数是多少。

感觉很简单啊……不知道为啥标成了hard。

可以像merge sort那样，每次都比较两个array最前面的元素的大小，把小的那个取出来，这样一直取啊取，如果两个array里面元素个数总数是偶数，取到第 ``n // 2`` 和第 ``n // 2 + 1`` 次（从0开始数）的时候就可以停止了，把最后两次取到的数算一算平均数就是中位数了；如果两个array里面元素个数总数是奇数，直接取到第 ``n // 2`` 次（从0开始数）的时候就可以停止了，这个第 ``n // 2`` 次取到的元素直接就是中位数了。
"""

from typing import *

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = (len(nums1) + len(nums2)) # 两个array里总共有多少个元素
        if n % 2 != 0: # 如果是奇数
            res = 0 # 记录最后一次取到的元素

            for _ in range(n // 2 + 1): # 取到第 n // 2 次的时候停止
                if nums1 != [] and nums2 != []: # 两个array都不为空
                    if nums1[0] < nums2[0]: # 比较两个array最前面的元素的大小。如果array1的比较小
                        res = nums1.pop(0) # 取出array1前面的元素
                    else: # array2的比较小或者相等
                        res = nums2.pop(0) # 取出array2前面的元素
                elif nums1 != []: # array2空了
                    res = nums1.pop(0) # 那只能从array1里面取最前面的元素了
                else: # array1空了
                    res = nums2.pop(0) # 只能从array2里面取最前面的元素了

            return float(res)
        else:
            res = [0, 0] # 记录倒数两次取到的元素

            for _ in range(n // 2 + 1): # 取到第 n // 2 次的时候停止
                if nums1 != [] and nums2 != []:
                    if nums1[0] < nums2[0]:
                        res[0], res[1] = res[1], nums1.pop(0) # 记录最后两次取到的元素
                    else:
                        res[0], res[1] = res[1], nums2.pop(0)
                elif nums1 != []:
                    res[0], res[1] = res[1], nums1.pop(0)
                else:
                    res[0], res[1] = res[1], nums2.pop(0)

            return sum(res) / 2 # 最后两次取到的元素做一次平均就是中位数了

# s = Solution()
# print(s.findMedianSortedArrays([1, 3], [2])) # 2.0
# print(s.findMedianSortedArrays([1, 2], [3, 4])) # 2.5
# print(s.findMedianSortedArrays([1], [2])) # 1.5