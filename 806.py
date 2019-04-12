"""
每个字母有一个宽度，每行的宽度是100，问你一个字符串需要占多少行，最后一行占了多宽。

和以前做过的一道排版题差不多，用一个buffer存未成行的缓存区，再用一个count记录已经排版好的行数。
"""

from typing import *

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        buffer = 0 # 还未成一整行的字符的总宽度
        typesetLineCount = 0 # 已经排满的行数

        for v in S:
            if buffer + widths[ord(v) - ord("a")] > 100: # 这行排不下了
                typesetLineCount += 1
                buffer = widths[ord(v) - ord("a")] # 当前字符只能另起一行
            else: # 这行还能排下当前字符
                buffer += widths[ord(v) - ord("a")]

        return [typesetLineCount + 1, buffer]

# s = Solution()
# assert s.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz") == [3, 60]
# assert s.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa")