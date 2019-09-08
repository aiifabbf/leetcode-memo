"""
把数字转换成罗马数字

就是13的反面。我这里用的方法是个十百千位分别处理。
"""

from typing import *

class Solution:
    def intToRoman(self, num: int) -> str:
        thousandTable = { # 千位可能的情况
            0: "",
            1: "M",
            2: "MM",
            3: "MMM", 
            4: "CM",
        }
        hundredTable = { # 百位可能的情况
            0: "",
            1: "C",
            2: "CC",
            3: "CCC",
            4: "CD",
            5: "D",
            6: "DC",
            7: "DCC",
            8: "DCCC",
            9: "CM",
        }
        tenTable = { # 十位可能的情况
            0: "",
            1: "X",
            2: "XX",
            3: "XXX",
            4: "XL",
            5: "L",
            6: "LX",
            7: "LXX",
            8: "LXXX",
            9: "XC"
        }
        oneTable = { # 个位可能的情况
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX"
        }
        # thousand = num // 1000 # 取出千位
        # hundred = (num - thousand * 1000) // 100 # 取出百位
        # ten = (num - thousand * 1000 - hundred * 100) // 10 # 取出十位
        # one = (num - thousand * 1000 - hundred * 100 - ten * 10) # 取出个位
        # 其实有更好的方法取出个十百千位
        thousand = num // 1000 % 10
        hundred = num // 100 % 10
        ten = num // 10 % 10
        one = num // 1 % 10
        # 总结一下就是n // b^k % b，其中b是进制，k是第k位
        return thousandTable[thousand] + hundredTable[hundred] + tenTable[ten] + oneTable[one]

# s = Solution()
# print(s.intToRoman(3))
# print(s.intToRoman(4))
# print(s.intToRoman(9))
# print(s.intToRoman(58))
# print(s.intToRoman(1994))