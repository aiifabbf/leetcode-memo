"""
把一个整数转换成7进制

很基础的数学题，直接用小学的做法就可以了，不停地整除7，结果就是把每次整除的余数记录下来，然后倒序排列。比如100

::

    100 / 7 = 14 ... 2
    14 / 7  = 2  ... 0
    2 / 7   = 0  ... 2
    0 / 7   = 0  ... 0
    0 / 7   = 0  ... 0
    ...

这样结果是 ``202`` 。

如果发现被除数是0，就不用再整除下去了。
"""

from typing import *

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num < 0: # 负数的话
            return "-" + self.convertToBase7(abs(num)) # 就转换它的绝对值，再在前面加一个负号
        else: # 正数
            res = [] # 用来记录余数
            
            while num != 0: # 不停地整除7，直到被除数是0为止
                res.append(num % 7) # 记下余数
                num = num // 7 # 商变成新的被除数

            return "".join(map(str, reversed(res))) # 结果就是每次整除的余数倒序排列

# s = Solution()
# print(s.convertToBase7(1)) # 1
# print(s.convertToBase7(7)) # 10
# print(s.convertToBase7(100)) # 202
# print(s.convertToBase7(-7)) # -10