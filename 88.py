"""
原地（in-place）合并两个已经从小到大排好序的array。

这个操作会出现在merge sort算法里面。具体做法是，不停地比较两个已经从小到大排好序的array的第一个元素的大小，取出小的那个放好，再继续比较，直到其中一个array空了，再把非空的那个array整个放过去。
"""

from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[:] = sorted(nums1 + nums2) # 这样不太好吧

        a = nums1[0: m]
        b = nums2[0: n]
        res = []

        while a and b: # 两个array都不为空
            if a[0] <= b[0]: # 比较两个array的第一个元素的大小，取出小的那个放入res
                res.append(a.pop(0)) # a的第一个元素比较小，所以取出来放好
            else:
                res.append(b.pop(0)) # b的第一个元素比较小，所以取出来放好
        
        if a: # a非空，说明b已经空了
            res += a # 把a整个直接放到res后面
        else: # b非空，说明a已经空了
            res += b # 把b整个直接放到res后面

        nums1[:] = res