"""
找两个array的最长公共substring（连续）的长度。

这种找两个array的公共部分的题一般用二维动态规划做。设 :math`p_{i, j}` 是以 :math:`b_i` 为最后一个元素、 :math:`a_j` 为最后一个元素的最长公共substring的长度。

那现在开始填表……

::

        0   1   2   3   4   A
    --------------------
    0  |
    1  |
    2  |
    3  |
    4  |
    B

大概是这么一张表格。初始条件是第一行和第一列。第一行不用说了，就是看B的第0个元素是否和A的各个元素相等，即 ``B[0] == A[j]`` ，如果相等，能形成长度为1的substring，所以这一个格子就填1，如果不相等，；第一列同理，看A的第0个元素是否和B的各个元素相等，即 ``A[0] == B[i]`` ，如果相等，这一个格子填1，不相等填0。

接下来是表格剩下的广大区域，关键是要想出状态转移方程。这里因为是substring，所以状态转移方程很简单

.. math::

    p_{i, j} = \left\{\begin{aligned}
            & p_{i - 1, j - 1} + 1, \qquad && a_j = b_i \\
            & 0,                    \qquad && a_j \neq b_i
        \end{aligned}\right.

简单来说

-   如果A的第j个元素和B的第i个元素相等，那么说明以A的第j - 1个元素为结尾的与以B的第i - 1个元素为结尾的公共substring可以继续接下去，所以公共长度就是上一个公共substring的长度加1
-   如果A的第j个元素和B的第i个元素不相等，那么无论怎样，以A的第j个元素结尾的所有的substring都不可能与以B的第i个元素结尾的任何一个substring相等，所以公共长度直接就是0。
"""

from typing import *

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = []
        firstLine = []
        maxLength = 0

        for v in A: # 处理初始状态。第一行
            if v == B[0]:
                firstLine.append(1)
            else:
                firstLine.append(0)
        
        maxLength = max(maxLength, max(firstLine))
        dp.append(firstLine)

        for rowIndex in range(1, len(B)):
            thisLine = []
            if B[rowIndex] == A[0]: # 处理初始状态。每一行的第一列
                thisLine.append(1)
            else:
                thisLine.append(0)

            for columnIndex in range(1, len(A)): # 填表
                if A[columnIndex] == B[rowIndex]: # 状态转移方程
                    thisLine.append(dp[-1][columnIndex - 1] + 1)
                else:
                    thisLine.append(0)
            
            maxLength = max(maxLength, max(thisLine)) # 一边填一边记录最大值，省得最后再遍历一遍
            dp.append(thisLine)

        # print(dp)

        return maxLength

# s = Solution()
# assert s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
# assert s.findLength([1, 2], [1, ]) == 1