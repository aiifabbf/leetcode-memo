"""
解析罗马数字

罗马数字里有几个基本符号

::

    I   1
    V   5
    X   10
    L   50
    C   100
    D   500
    M   1000

几个典型数字

::

    I   1
    II  2
    III 3
    IV  4
    IX  9
    XI  11
    XII 12
    XIII    13
    XIX 19
    XX  20
    XXX 30
    XL  40
    LX  60

发现规律了吗？当后一个数字比前一个数字大的时候，表示后一个数字减去前一个数字；而如果后一个数字小于等于前面一个数字的时候，就是简单的把两个数字加起来。

所以我们就遍历每个字符，看当前字符表示的数字和前面一个字符表示的数字的关系，如果发现当前数字小于等于前面一个数字，直接把结果加上当前数字；如果发现当前数字比前一个数字大，就把结果加上当前数字、减去前一个数字、 **然后再减去一次前一个数字** ，因为遍历到前面一个字符的时候，并不知道后面一个字符代表的数字会大于前面一个字符代表的数字，所以要减去前面一次误加的数字。
"""

from typing import *

class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        } # 基本字符到数字的转换表
        last = s[0] # 记录上一个字符
        res = table[last] # 记录结果

        for v in s[1: ]: # 从第1个字符开始遍历
            if table[v] > table[last]: # 发现当前字符代表的数字大于前面一个字符代表的数字
                res = res - table[last] + table[v] - table[last] # 要先减去上次误加的数字，再加上当前数字减前一个数字
            else: # 当前字符代表的数字小于等于前面一个字符代表的数字
                res = res + table[v] # 直接加上当前数字就好了
            last = v

        return res

# s = Solution()
# print(s.romanToInt("III")) # 3
# print(s.romanToInt("IV")) # 4
# print(s.romanToInt("IX")) # 9
# print(s.romanToInt("LVIII")) # 58
# print(s.romanToInt("MCMXCIV")) # 1994