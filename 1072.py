"""
给n个数字，可以无限次选择这些数字的某一个位，全部翻转，问最后最多可以有多少个数字是 :math:`2^n - 1` （也就是是0或者全1）。

比如

::

    0 1
    1 0

这两个数字，可以选择第2列，把它们全部翻转一次，这样这两个数字就变成了

::

    0 0 -> 2^0 - 1
    1 1 -> 2^2 - 1

这样两个数字都可以写成 :math:`2^n - 1` 的形式，所以最多可以有2个数字。

所以对于一个数字，可以选择2种翻转方案中的其中一种

-   要么把所有0都变成1，这样整个数字变成 ``111...111``
-   要么把所有1都变成0，这样整个数字变成 ``000...000``

可以用一个 ``Counter`` 记录一下n个数字的所有翻转方案，这样可能出现两种情况

-   n个数字没有共享任何一种翻转方案

    也就是说没有办法选择一种翻转方案，使得2个或者2个以上的数字同时变成全0或者全1，而只能选择某一种翻转方案，使1个数字变成全0或者全1。

    此时答案是1。

-   有一些翻转方案可以使多个数字同时变成全0或者全1

    也就是说存在一种翻转方案，可以使得多个数字同时变成全0或者全1。

    选择其中出现频次最高的那种方案出现的次数就是答案。

这两种情况都可以统一为取出现频次最高的那种翻转方案的出现的次数。
"""

from typing import *

import collections

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        positions = [] # 所有的翻转方案

        for row in matrix: # 遍历n个数字
            thisZerosToOnesPositions = [] # 当前数字翻转0，变成全1的翻转方案
            thisOnesToZerosPositions = [] # 当前数字翻转1，变成全0的翻转方案

            for columnIndex, box in enumerate(row):
                if box == 0: # 如果当前位是0，可以翻转一次变成1
                    thisZerosToOnesPositions.append(columnIndex)
                else: # 如果当前位是1，可以翻转一次变成0
                    thisOnesToZerosPositions.append(columnIndex)

            positions.append(tuple(thisZerosToOnesPositions)) # 记录0变1的翻转方案
            positions.append(tuple(thisOnesToZerosPositions)) # 记录1变0的翻转方案

        counter = collections.Counter(positions) # 记录每一种翻转方案的出现频次
        return counter.most_common(1)[0][1] # 出现频次最高的那种翻转方案的频次就是答案

# s = Solution()
# print(s.maxEqualRowsAfterFlips([[0,1],[1,1]])) # 1
# print(s.maxEqualRowsAfterFlips([[0,1],[1,0]])) # 2
# print(s.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]])) # 2