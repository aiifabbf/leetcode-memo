"""
按要求重新排列一组字符串。规则是，先把字符串按第一个空格分开，前半部分不看，看后半部分，如果后半部分的第一个字符是数字，归到数字一类；如果后半部分的第一个字符是字母，归到字母一类。然后数字一类不用排序，按顺序排列；字母一类先按后半部分字典排序，如果后半部分相同，再按前半部分字典排序。

数字一类很好办，直接用 ``filter()`` 过滤出来。

字母一类其实也很简单，先用 ``filter()`` 过滤出来，然后在 ``sorted()`` 里面用自定义的key来排序，可以选择 ``(后半部分, 前半部分)`` 也就是 ``v.split(" ", 1)[:: -1]`` 来作为custom key排序。 ``str.split()`` 的第二个参数是指定做多少次拆分。
"""

from typing import *

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        sortedAlphaList = sorted(filter(lambda v: v.split(" ", 1)[1][0].isalpha(), logs), key=lambda v: v.split(" ", 1)[:: -1])
        sortedNumbericList = list(filter(lambda v: v.split(" ", 1)[1][0].isdigit(), logs))
        return sortedAlphaList + sortedNumbericList

# s = Solution()
# print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])) # ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
# print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"])) # ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]