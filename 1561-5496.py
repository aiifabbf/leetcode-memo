"""
.. default-role:: math

你和Alice、Bob总共三个人玩石头游戏，场上有 `3n` 堆石头，每轮你随便选出3堆石头，Alice会拿走这3堆里石头最多的那堆，你再从剩下的2堆里选一堆，最后Bob拿剩下的一堆。问你最多能拿多少石头。

.. 怎么这么喜欢玩石头游戏……

大胆猜测，不如你每一回就拿最大的两堆+最小的一堆，让Alice拿其中最大的一堆，自己拿中间不大不小的那堆，Bob拿最小的一堆。结果还真就对了。
"""

from typing import *

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        array = sorted(piles)
        res = 0

        while array:
            array.pop() # Alice拿最大的
            res += array.pop() # 我拿不大不小的
            array.pop(0) # Bob拿最小的

        return res

s = Solution()
print(s.maxCoins([2, 4, 1, 2, 7, 8]))
print(s.maxCoins([2, 4, 5]))
print(s.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]))