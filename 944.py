"""
删除一些列，使得每列的字母正好从小到大排序。

不太明白这题到底有什么意义。
"""

from typing import *

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        
        for columnIndex in range(len(A[0])):
            column = [row[columnIndex] for row in A]
            if sorted(column) != column:
                count += 1

        return count