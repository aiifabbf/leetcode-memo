r"""
array里的元素 :math:`a_i` 代表第i天的气温。现在要生成另一个array，里面的元素 :math:`b_i` 代表在第i天之后要等多少天，才能等到气温大于第i天的那天。

换句话说，要从第i+1天开始找，从 :math:`\{a_{i + 1}, a_{i + 2}, ...\}` 里找到一个 :math:`a_j > a_i` ， 这样 :math:`b_i = j - i` 。如果不存在这样的 :math:`j` ，就令 :math:`b_j = 0` 。

最暴力的做法当然就是每次都去第i天后面找比当前的值大的元素，如果不巧array刚好是严格递减的，复杂度是 :math:`O(n^2)` 。

.. 一开始我在想有没有优化这个搜索的方法，是不是能把第i次搜索的结果缓存起来给第i+1次用，但是很可惜我想了很久也没有想到。最后看了一下topics，说是stack。我马上就懂了……

做法是维护一个stack，里面放数对 ``(i, v)`` ，第一个元素是日期，第二个元素是这一天的气温。每次遇到一个元素，先看stack顶部这一天的气温和这个元素比，哪个大，如果stack顶部的气温比这个元素小，那么就出stack，并且把出stack的这个元素代表的那天的位置置为今天和这一天日期的差 [#]_ 。然后继续比较，直到stack空了，或者stack顶部那天的气温大于或等于今天的气温，最后再把今天的日期、今天的气温放进stack顶部，给后面几天做比较。

.. [#] 这就是为什么stack里面放的不只是单单一个气温，而要把日期也一起放进去，不然你也不知道到底是哪一天。
"""

from typing import *

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # stack = [
        #     (0, T[0])
        # ]
        stack = [] # stack里的元素保证从底到顶递减（不是严格递减，可以相等）
        res = [0] * len(T) # 先初始化，每天都假设永远等不到气温比今天高的那天，这样最后不用补0什么的，方便一点

        for i, v in enumerate(T):
            if stack:

                while True:
                    if stack:
                        day = stack.pop() # 这里pop了，后面如果发现大于等于今天的气温，记得要放回去
                        if v > day[1]: # 和stack顶部的元素比较，如果今天气温大于这一天的气温，说明那一天找到了离自己最近的、比自己气温高的那一天
                            res[day[0]] = i - day[0] # 把那一天的值设为今天和那一天的日期之差
                        else: # 发现今天气温小于等于那一天的气温，那么说明那一天至今都没有找到比自己气温高的日子，同时因为stack保证气温递减，所以顶部以下的日子都不用看了，能保证顶部以下的所有日子的气温都大于等于顶部那天的气温。
                            stack.append(day) # 记得把那一天放回去
                            stack.append((i, v)) # 再把今天放进去
                            break # 继续明天
                    else: # stack已经空了，没日子好比较了
                        stack.append((i, v)) # 直接把今天放进去
                        break # 继续明天

            else: # stack空的话，就直接放进去
                stack.append((i, v))
        return res # 初始化的好处就是最后直接返回，不用补零什么的

# s = Solution()
# print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))