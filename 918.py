r"""
.. default-role:: math

求一个循环列表的最大substring和，要求这个substring的长度不能超过循环列表的一个循环的长度。

一个普通的列表的最大substring和是非常简单的（其实也不简单，我刚开始学DP的时候也完全没法理解这件事），用DP可以做到 `O(n)` 。所以这道题自然而然就能想到用DP，也就是每次把列表的第一个元素拿出来、放到列表的最后，然后用DP求一次最大substring和。

求一个长度 `n` 的列表的最大substring和复杂度是 `O(n)` ，这里这个“把列表的第一个元素拿出来、放到列表的最后”这个操作要做 `n` 次，才能穷尽所有可能的情况，所以这个做法有点暴力，复杂度是 `O(n^2)` ，看题目的要求里的数据规模，应该是过不了的，题目应该是希望接受一个 `O(n)` 或者 `O(n \ln n)` 的做法。

不知道怎么回事又想到了积分的做法……在普通的单向列表里也可以用积分的做法来找最大substring和，但是复杂度比DP稍微高一点，是 `O(n \ln n)` 

1.  积分
2.  遍历每个积分值 `S_j` ，往前找最小的 `S_i` ， `S_j - S_i` 就是以第j个元素结尾的最大substring和，记为 `M_j`
3.  遍历完之后， `\max\{M_j\}` 就是全局的、整个单向列表的最大substring和

这样其实和暴力做法没什么区别，原因出在第2步里，遍历到每个积分值 `S_j` 的时候，都要往前遍历一遍，找到最小的 `S_i, i < j` ，这个操作的复杂度是 `O(n)` ，所以使得整个做法的复杂度变成了 `O(n^2)` 。可以用heap把这个操作的复杂度降低到 `O(\ln n)` ，这样整个算法的复杂度就降低到 `O(n \ln n)` 了

1.  积分
2.  用一个heap保存见过的积分值
3.  遍历每个积分值 `S_j` ，从heap里找最小的 `S_i` （这个操作是从heap里取最小的元素，复杂度是 `O(1)` ，但是取完之后还要维护heap结构，复杂度是 `O(\ln n)` ，所以整个操作的复杂度被强行拉高到 `O(\ln n)` ）， `S_j - S_i` 就是以第j个元素结尾的最大substring和，记为 `M_j` 。同时记得把 `S_j` 放到heap里（这个操作是往heap里插入元素，复杂度是 `O(\ln n)` ）
4.  同理，遍历完之后， `\max\{M_j\}` 就是全局的、整个单向列表的最大substring和

用了heap之后整个算法的复杂度就降低到 `O(n \ln n)` 了。

循环列表有一点不太一样，我们需要把这个列表复制一次，再头尾相接，在python里直接就是 ``A + A`` ，然后再积分。

此外，题目还要求取得最大substring和的那个substring的长度不能超过原列表的长度，就是不能超过 ``A`` 的长度。这个要求也很容易理解，如果没有这个要求的话，设想一个全是正数的循环列表

::

    1 2 3 4

你可以取一个无限长度的substring

::

    1 2 3 4 1 2 3 4 1 2 3 4 ...

最大substring和是无穷大。

解决办法是，heap不止需要存 `S_i` ，还需要存位置 `i` ，也就是存一个tuple。这样从heap里取最小 `S_i` 的时候，可以知道这个最小的积分项是否在一个 ``A`` 的长度之内。
"""

from typing import *

import itertools
import heapq

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        integral = [0] + list(itertools.accumulate(A + A)) # 因为是循环列表，所以需要求A + A的积分。这样integral[j] - integral[i] == sum(A[i: j])
        length = len(A) # 因为题目要求substring的长度不能超过A的长度
        res = float("-inf") # 记录目前为止的最大和
        heap = [
            (integral[0], 0)
        ]
        heapq.heapify(heap) # 用一个heap来存之前见过的积分值和位置，这样的话，寻找最小值的复杂度是O(1)（当然后续还有一个O(ln n)维护heap的操作）、插入的复杂度是O(ln n)

        for i, v in enumerate(integral[1: ], 1): # 遍历积分值
            while True:
                smallest, position = heapq.heappop(heap) # 往前找找，找最小的积分值
                if position >= i - length: # 可是还需要满足substring长度不超过A的长度的要求
                    res = max(res, v - smallest)
                    heapq.heappush(heap, (smallest, position)) # pop完了记得放回去
                    break
                # else: # 如果substring的长度在遍历到第i个的时候超过了A的长度，那么到第i+1个的时候肯定也是超过的，所以pop之后不用push回来，反正没有用了
                #     pass

            heapq.heappush(heap, (v, i)) # 记得把当前积分值和位置push回去

        return res

# s = Solution()
# print(s.maxSubarraySumCircular([1, -2, 3, -2])) # 3
# print(s.maxSubarraySumCircular([5, -3, 5])) # 10
# print(s.maxSubarraySumCircular([3, -1, 2, -1])) # 4
# print(s.maxSubarraySumCircular([3, -2, 2, -3])) # 3
# print(s.maxSubarraySumCircular([-2, -3, -1])) # -1
# print(s.maxSubarraySumCircular([3, 1, 3, 2, 6])) # 15