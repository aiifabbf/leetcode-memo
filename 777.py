# X是空格，R是只能往右走，L是只能往左走，R和L不能互相穿越

from typing import *

# import collections
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # if collections.Counter(start) != collections.Counter(end):
        #     return False

        if start.replace("X", "") == end.replace("X", "") and int(end.replace("X", "0").replace("L", "2").replace("R", "1"), base=3) >= int(start.replace("X", "0").replace("L", "2").replace("R", "1"), base=3):
            return True
        return False

s = Solution()
print(s.canTransform("RXXLRXRXL", "XRLXXRRLX"))