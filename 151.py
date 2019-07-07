"""
颠倒单词。

可能不用str内建方法是有点难……
"""

from typing import *

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

# s = Solution()
# print(s.reverseWords("the sky is blue"))
# print(s.reverseWords("  hello world!"))
# print(s.reverseWords("a good   example"))