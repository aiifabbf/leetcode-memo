from typing import *

# class Solution:
#     def findKthNumber(self, m: int, n: int, k: int) -> int:
#         l = sorted(i * j for i in range(1, m + 1) for j in range(1, n + 1))
#         return l[k - 1]

#         # 最naive办法，不能过，memory limit exceed。

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        


s = Solution()
print(s.findKthNumber(3, 3, 5))
print(s.findKthNumber(2, 3, 6))