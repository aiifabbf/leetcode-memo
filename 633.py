r"""
判断一个数n能否写成最多两个整数的平方和，正好写成一个完全平方数也是可以的。

先测n自己是不是就是完全平方数，如果是的话最好；如果不是，就把 :math:`[1, \lfloor\sqrt{n}\rfloor]` 每一个都遍历过去，看 :math:`n - i^2` 是不是完全平方数。因为如果一个数可以正好写成两个数的平方和，那么说明这个数减去一个完全平方数，剩下的部分仍然是一个完全平方数。

想起了279题。
"""

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        for i in range(1, math.floor(math.sqrt(c)) + 1): # 试一遍[1, floor(sqrt(n))]里的数就够了
            if self.isSquareNumber(c - i ** 2): # 如果减去一个完全平方数，剩下的部分仍然是一个完全平方数
                return True # 那么成了
        else: # 扫描了这么多数都没有成功
            return False # 说明必须要写成2个以上整数的平方和
    
    def isSquareNumber(self, n: int) -> bool: # 判断一个数是不是完全平方数
        greatestSquareLessThanOrEqualN = math.floor(math.sqrt(n))
        if greatestSquareLessThanOrEqualN ** 2 == n:
            return True
        else:
            return False

# s = Solution()
# assert s.judgeSquareSum(5) == True
# assert s.judgeSquareSum(3) == False
# assert s.judgeSquareSum(4) == True
# assert s.judgeSquareSum(0) == True
# assert s.judgeSquareSum(1) == True
# assert s.judgeSquareSum(2) == True