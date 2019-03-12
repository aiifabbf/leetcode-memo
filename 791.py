from typing import *

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        return "".join(sorted(T, key=S.find))

s = Solution()
print(s.customSortString("cba", "abcd"))