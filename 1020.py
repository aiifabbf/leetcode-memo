"""
有没有可能把一个array分成三段累加和相等的substring？

一开始想到的方法当然就是一个一个去试，但是发现会超时。

后来突然想到积分的方法，先给array做一个积分，那么这样积分序列的最后一个值就是整个数列的和，积分序列里第i个数的值是array里从第0个到第i个的substring的和。这样，所谓分成三段累加和相等的substring，就是从这个积分序列里找1/3分位点、2/3
"""

from typing import *

import itertools

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        else:
            # summation = sum(A)
            # summation1 = 0
            # summation2 = summation - summation1

            # for i in range(1, len(A) - 1):
            #     summation1 += A[i - 1]
            #     summation2 = summation - summation1

            #     for j in range(i + 1, len(A)):
            #         # print(i, j, summation1, summation2)
            #         summation2 -= A[j - 1]
            #         if summation1 == summation2 == summation - summation1 - summation2:
            #             return True

            # return False
            # 一改：超时了
            integral = list(itertools.accumulate(A)) # 先做个积分
            secondProportion = integral[-1] * 2 / 3 # 2/3分位点的值
            firstProportion = integral[-1] / 3 # 1/3分位点的值

            try:
                firstSlicePosition = integral.index(firstProportion) # 看看是否存在1/3分位点
                try:
                    secondProportion = integral.index(secondProportion, firstSlicePosition + 1) # 而且需要2/3分位点在1/3分位点之后
                    return True
                except:
                    return False
            except:
                return False

# s = Solution()
# assert s.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])
# assert not s.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
# assert s.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])
# assert s.canThreePartsEqualSum([18,12,-18,18,-19,-1,10,10])
# assert not s.canThreePartsEqualSum([6,1,1,13,-1,0,-10,20])
# assert s.canThreePartsEqualSum([29,31,27,-10,-67,22,15,-1,-16,-29,59,-18,48])