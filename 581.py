# 找到数列中的某个子序列（连续的substring），使得只需要sort这个substring就可以使得整个数列排序完成。要求得到能满足这样要求的substring的最小长度。

from typing import *

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        把排序好的数列和原数列做一个diff。

        先把数列排一遍，然后看这个排列好的数列和原数列有哪些位置不同。如果没有，说明数列本身就是排列好的，这样直接返回0；如果有，看最左的位置是哪个，最右的位置是哪个，减一下再+1，就得到了最短substring的长度。

        为什么要取最左和最右？如果不取最左或者最右，说明只排中间的substring就可以使得整个数列排好，但是这是不可能的，这样就会遗漏掉一些元素。
        """
        sortedNums = sorted(nums)
        left = 0
        right = len(nums) - 1
        for i in range(0, len(nums)):
            if nums[i] != sortedNums[i]:
                left = i
                break
        else:
            return 0

        for i in range(0, len(nums))[:: -1]:
            if nums[i] != sortedNums[i]:
                right = i
                break

        return right - left + 1
        # 据说还有更好的 :math:`O(n)` 的做法。

s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(s.findUnsortedSubarray([1, 2, 3, 4]))