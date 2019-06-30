r"""
有m颗糖发给n个人，发的规则是

-   给第1个人1颗糖
-   给第2个人2颗糖
-   给第3个人3颗糖
-   ...
-   给第n个人n颗糖
-   给第1个人n+1颗糖
-   给第2个人n+2颗糖
-   ...
-   给第n个人n+n颗糖
-   给第1个人n+n+1颗糖
-   ...

中间如果发现糖不够发了，就把剩下的所有的糖都给后面一个人。问每个人得到多少糖。

可以直接暴力做，不要看糖的数量是10^9，其实复杂度并不高，因为n项等差数列求和的结果是 :math:`O(n^2)` 阶的，所以其实暴力做的复杂度是 :math:`O(\sqrt{m})` 其中m是糖的个数。

.. 亏我还花了40 min推通项公式，输了输了。
"""

from typing import *

import itertools

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # n = num_people
        # k = 0

        # while True:
        #     allCandiesUntilThisLevel = sum(range(1, k * n + n + 1))
        #     if candies - allCandiesUntilThisLevel < 0:
        #         break
        #     else:
        #         k = k + 1

        # k = k - 1
        # allCandiesUntilThisLevel = sum(range(1, k * n + n + 1))
        # remainingCandies = candies - allCandiesUntilThisLevel
        # if k == -1:
        #     res = [0] * n
        # else:
        #     res = [(1 + k) * k * n // 2 + (k + 1) * i for i in range(1, n + 1)]

        # for i in range(1, num_people + 1):
        #     extraCandiesToThisPerson = (k + 1) * n + i
        #     if remainingCandies <= extraCandiesToThisPerson:
        #         res[i - 1] += remainingCandies
        #         return res
        #     else:
        #         res[i - 1] += extraCandiesToThisPerson
        #         remainingCandies -= extraCandiesToThisPerson
        # 
        # return res
        # 一改：暴力做法更好

        res = [0] * num_people # 一开始大家都没有糖
        candyForThisPerson = 1 # 应该给当前这个人的糖的个数

        for i in itertools.cycle(range(len(res))): # 用一个cycle反复遍历这n个人
            if candies < candyForThisPerson: # 如果发现手里的糖不够发了
                res[i] += candies # 就把手里剩下的所有的糖给当前这个人
                return res
            else: # 如果手里的糖够发
                res[i] += candyForThisPerson # 按规定发糖
                candies -= candyForThisPerson # 手里的糖减少
                candyForThisPerson += 1 # 发给下一个人的糖的个数要+1

        return res

# s = Solution()
# print(s.distributeCandies(7, 4)) # [1, 2, 3, 1]
# print(s.distributeCandies(10, 3)) # [5, 2, 3]
# print(s.distributeCandies(10, 4)) # [1, 2, 3, 4]
# print(s.distributeCandies(60, 4)) # [15, 18, 15, 12]