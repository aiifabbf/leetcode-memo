"""
某种奇怪的纸牌游戏……有一个array（这里既然没有顺序，其实应该用Set更好）表示一系列纸牌，然后步骤是这样的

1.  拿出第一张牌，放到一边
2.  拿出第一张牌，放到牌堆的末尾
3.  回到第一步，直到没牌为止

问你一开始这个纸牌的顺序应该是怎样的，才能做到所有放到一边纸牌是递增的。

太绕了。举个例子，比如 ``[2,13,3,11,5,17,7]`` 这样的纸牌堆

1.  取出2

    此时2放到一边了，牌堆变成了 ``[13,3,11,5,17,7]``

2.  把13放到牌堆末尾

    牌堆变成了 ``[3,11,5,17,7,13]``

3.  取出3

    此时3放到一边了，牌堆变成了 ``[11,5,17,7,13]``

4.  ...

我的思路是做一个逆过程，既然你的正过程是

1.  最前元素出
2.  最前元素出、放到最后

那么逆过程就是

1.  最后元素出、放到最前
2.  元素进、放到最前
"""

from typing import *

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck) # 桌子一边的元素
        queue = [deck.pop()]

        while deck:
            queue.insert(0, queue.pop()) # 最后的元素出、放到最前
            queue.insert(0, deck.pop()) # 元素进、放到最前

        # print(queue)
        return queue

s = Solution()
assert s.deckRevealedIncreasing([17,13,11,2,3,5,7]) == [2,13,3,11,5,17,7]