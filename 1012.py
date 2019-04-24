r"""
问[1, n]之间有多少个数，其十进制表示里存在重复的数字。比如 ``112`` 含有两个1。

可以先考虑这个问题的反面，即寻找[1, n]之间有多少个数，其十进制表示里 **不** 存在重复的数字。

这个问题可以分成两部分操作来做，假设n是一个k位数。第一部分是这样的

1.  先数一位数里有多少个满足条件的数

    一位数的话，就是集合 :math:`\{1, 2, ..., 9\}` 的大小，一共9个。

2.  数两位数里有多少个满足条件的数

    两位数的话，区间是 :math:`[10, 100)` 。
    
    首先选十位的数字，因为已经限定是两位数，所以第一位不能是0，所以第一位可以从集合 :math:`\{1, 2, ..., 9\}` 里选一个数，一共9种选择，假设选择的是 :math:`x` ；到第二位的时候，可以选0，可选的集合坍缩成了 :math:`\{0, 1, 2, ..., 9\} \backslash \{x\}`  ，一共9种选择。

    十位和个位的选择虽然不独立，但是仍然可以用乘法定理，所以两位数里满足条件的个数总共是 :math:`9 \times 9 = 81` 。

    到这里还是仍然看不出任何规律。

3.  数三位数里有多少个满足条件的数

    三位数的话，区间是 :math:`[100, 1000)` 。

    首先选择百位的数字，因为已经限定是三位数，所以第一位不能是0，所以百位上的数字除去0以外只有9种选择；到了十位的时候，可以选0了，所以还是有9种选择；到了个位的时候，也是可以选0的，但是十位已经选择了某个数，所以个位只有8种选择。

    这样三位数里满足条件的数总共有 :math:`9 \times 9 \times 8 = 648

4.  ...
5.  数i位数里有多少个满足条件的数

    经过一位数、两位数、三位数的分析已经足够看出规律了，k-1位数里满足条件的数总共有 :math:`9 \times A_9^{i-1}`

6.  ...
7.  数k-1位数里有多少个满足条件的数


第二部分是这样的

1.  数最高位小于n的最高位的所有k位数里，有多少个满足条件的数

    因为我们限定了k位数，所以最高位不能是0，同时最高位不能超过原来的那个数的最高位的数字。

    最高位之后的数字就可以随便选了，只要和前面的都不重复就可以了。

2.  数最高位和n相同、第二高位小于n的第二高位的所有k位数，里有多少个满足条件的数

    保持最高位和原数字的最高位相同，同时第二高位要小于原数字的第二高位、并且和最高位不能重复。

    剩下的数字随便选就可以了。

3.  数最高位、第二高位和n相同、第三高位小于n的第三高位的所有k位数里，有多少个满足条件的数

    从这里开始要另外注意一件事情，就是原数字的最高位、第二高位 **有可能是重复的** ，这时候，直接退出就可以了，因为已经数完了。

    如果原数字的最高位、第二高位没有重复，那就还是照前两步的做法一样做：第三位要小于原数字的第三位、同时和最高位、第二高位不能重复。

    剩下的数字就在不重复的基础上随便选了。

4.  ...
5.  数除了个位和n不同、其他位和n全部相同的所有k位数里，有多少个满足条件的数

面试头条被问到这道题了，但是当时没做出来，尴尬。
"""

from typing import *

import math

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        return N - self.numberOfPositiveIntegersWithoutRepeatedDigitLessThanN(N + 1)

    def numberOfPositiveIntegersWithoutRepeatedDigitLessThanN(self, n: int) -> int: # 得到[1, n)区间内，十进制各位都没有出现重复数字的数字的个数
        listN = list(map(int, str(n)))
        if len(listN) == 1:
            return n - 1
        else:
            res = 0
            k = len(listN)

            for i in range(1, k): # 数i位数里有多少个满足条件的数，数到k-1位数为止
                res = res + 9 * self.A(9, i - 1) # 最高位不能是0，所以有9种情况。选完之后还有9个数字可选、分配给剩下的i-1位，所以是A(9, i-1)。

            res = res + (listN[0] - 1) * self.A(9, k - 1) # 最高位不为0、同时小于原数字最高位的n位数字的组合数

            for i, v in enumerate(listN[1: ], 1): # 从最高位、一直到第i-1位都和原数字相同的组合数
                prefix = listN[: i] # 最高位到第i-1位。相当于一个前缀
                if i != len(set(prefix)): # 如果前缀出现了重复数字，就没必要再算下去了
                    break
                else:
                    thisDigitSelectable = set(range(v)) - set(prefix) # 当前这个位（第i位）的数字，既不能和前面的数字重复、也不能超过原数的这一位的数字
                    res = res + len(thisDigitSelectable) * self.A(10 - (i + 1), k - (i + 1)) # 剩下的k-(i+1)位数字可以从10个数字去掉第i位选的数字、去掉前i位选的数字的剩下的10-(i+1)个数字里选。

            return res

    def A(self, m: int, n: int):
        return math.factorial(m) // math.factorial(m - n)

# s = Solution()
# print(s.numberOfPositiveIntegersWithoutRepeatedDigitLessThanN(21)) # 19
# print(s.numberOfPositiveIntegersWithoutRepeatedDigitLessThanN(101)) # 90
# print(s.numberOfPositiveIntegersWithoutRepeatedDigitLessThanN(1001)) # 738
# print(s.numberOfPositiveIntegersWithoutRepeatedDigitLessThanN(109 + 1)) # 98

# print(s.numDupDigitsAtMostN(1)) # 0
# print(s.numDupDigitsAtMostN(10)) # 0
# print(s.numDupDigitsAtMostN(20)) # 1
# print(s.numDupDigitsAtMostN(100)) # 10
# print(s.numDupDigitsAtMostN(1000)) # 262
# print(s.numDupDigitsAtMostN(109)) # 11