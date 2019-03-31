"""
每次修改array之后，array里所有的偶数之和是多少。
"""

from typing import *

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        summation = sum(v for v in A if v % 2 == 0)
        res = []

        for query in queries:
            value = query[0]
            index = query[1]
            if A[index] % 2 == 0 and value % 2 == 0: # 这个数本来就是偶数，已经在summation里面了，然后又加了一个偶数，结果还是偶数
                summation += value
            elif A[index] % 2 == 0 and value % 2 != 0: # 这个数本来就是个偶数，已经在summation里面了，但是加了个奇数，所以结果是奇数，要从summation里去掉
                summation -= A[index]
            elif A[index] % 2 != 0 and value % 2 == 0: # 这个数本来不是奇数，所以也不在summation里面，加了一个偶数，结果还是奇数，所以也没啥可做的
                pass
            else: # 这个数本来不是奇数，不在summation里面，但是加了个奇数，结果是偶数，要加入summation
                summation += value + A[index]
            A[index] += value # 这里有副作用……
            res.append(summation)

        return res

# s = Solution()
# print(s.sumEvenAfterQueries([1, 2, 3, 4], [
#     [1, 0],
#     [-3, 1],
#     [-4, 0],
#     [2, 3]
# ]))