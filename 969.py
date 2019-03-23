"""
让你用一种奇怪的方法给array排序，给出步骤。

这种方法是每步只颠倒array前面的k个元素。

先考虑一个最简单的情况，如果这个array里最大的元素的下标是i，怎样把这个最大的元素从i移到array的最后呢？

1.  先颠倒前i + 1个元素

    这样第i个元素就变成了array的第0个元素。

2.  颠倒整个array

    这样第0个元素、也就是刚才的第i个元素就变成了array的最后一个元素。

这样最大元素就排好了，再取array的前n - 1个，递归地、用同样的方法排列这个substring，直到substring为空。

题目的要求是颠倒总次数不能超过10 * n，那按照上面的方法，最差情况是2 * n，是满足题目的要求的。
"""

from typing import *

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if A:
            maximumPosition, maximum = max(((i, v) for i, v in enumerate(A)), key=lambda x: x[1]) # 得到最大元素的位置和最大元素的值
            B = (A[: maximumPosition + 1][:: -1] + A[maximumPosition + 1: ])[:: -1] # 先颠倒前i + 1个元素、再颠倒整个array。虽然用切片慢了点但是没有副作用我喜欢。
            return [maximumPosition + 1, len(A)] + self.pancakeSort(B[: -1]) # 递归地排列前n - 1个元素的substring
        else:
            return []