"""
找到第一个bad version

就是在 ``[1, 2, 3, ..., n]`` 中，从某个j开始往后一直到n都是bad version，要你找到这个j。

其实就是二分搜索，把它看成从含有重复元素的递增array ``[0, 0, 0, ..., 1, 1, 1]`` 里找到最左边第一个1的问题。
"""

from typing import *

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 4:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n + 1

        while left < right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1

        return left # 这里不会出现找不到的情况，所以直接return，不用像模板里写的那样再判断一次。

# s = Solution()
# print(s.firstBadVersion(500))