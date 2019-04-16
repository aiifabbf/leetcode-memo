"""
给一个整数n，问你需要多少步才能让它变成1。

可采取的步骤只有两种

-   如果n是偶数，只能除以2
-   如果n是奇数，可以选择加1或者减1

可以用递归的方法解决。
"""

from typing import *

import functools

class Solution:
    @functools.lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            if n % 2 == 0: # 如果n是偶数
                return self.integerReplacement(n // 2) + 1 # 只有一种可以采取的行动就是除以2
            else: # 如果n是奇数
                return min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1 # 有两种可以采取的行动，至于哪一种用的步骤少，那就都试一下吧

# s = Solution()
# assert s.integerReplacement(8) == 3
# assert s.integerReplacement(7) == 4