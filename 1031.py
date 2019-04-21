"""
array里取两个相互不重合的substring，一个substring长度是L、另一个长度是M，这两个substring的加和最大是多少？

我的思路是每次把array分成前后两段，这样可以避免重合的问题，然后前一段里扫描长度L的substring、后一段扫描长度M的substring，再前一段扫描长度M的substring、后一段扫描长度为L的substring（因为题目没说长度为L的substring一定要出现在长度为M的substring之后）。

从一个array里找到加和最大的固定长度的substring只需要从左往右扫描一遍，所以复杂度是 :math:`O(n)` 。这里要先给array分区，把array先分成前后两块，分别扫描，分区这个操作其实就是遍历，所以复杂度是 :math:`O(n)` 。所以整个程序的复杂度是 :math:`O(n^2)` ，但是这道题能过，所以就这么做了。
"""

from typing import *

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        L, M = min(L, M), max(L, M)
        maximumSummation = 0

        for i in range(L, len(A) - L): # 把array分成前后两段
            maximumSummation = max(maximumSummation, self.maxSubstringSumWithFixedLength(A[: i], L) + self.maxSubstringSumWithFixedLength(A[i: ], M), self.maxSubstringSumWithFixedLength(A[: i], M) + self.maxSubstringSumWithFixedLength(A[i: ], L)) # 前一段扫L、后一段扫M，还有前一段扫M、后一段扫L，因为题目没有说L一定出现在M之前

        return maximumSummation

    def maxSubstringSumWithFixedLength(self, array: List[int], length: int) -> int: # 扫描，得到固定长度的substring的最大和
        if array:
            if length > len(array): # 如果要求的长度都大于array本身的长度了，那么根本就不可能存在这样的substring
                return 0
            else:
                maximumSummation = 0
                summation = sum(array[: length]) # 这里避免重复计算、降低复杂度的重点是把summation缓存起来，不要每次都重新计算
                maximumSummation = max(maximumSummation, summation)

                for i in range(1, len(array) - length + 1):
                    summation = summation - array[i - 1] + array[i - 1 + length] # 窗口往后移动了一格，就把之前最前面的元素从summation里面删掉，再加上当前窗口的最后一个元素
                    maximumSummation = max(maximumSummation, summation)

                return maximumSummation
        else:
            return 0

s = Solution()
print(s.maxSubstringSumWithFixedLength([0,6,5,2,2,5,1,9,4], 2)) # 13
print(s.maxSubstringSumWithFixedLength([2,1,5,6,0,9], 4)) # 20
print(s.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2)) # 20
print(s.maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0], 3, 2)) # 29
print(s.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8], 4, 3)) # 31
print(s.maxSumTwoNoOverlap([1, 0, 3], 1, 2)) # 4
print(s.maxSumTwoNoOverlap([4,5,14,16,16,20,7,13,8,15], 3, 5)) # 109