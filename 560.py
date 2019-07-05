"""
array里有多少个substring的和是K？

和974类似，974求的是array里多少个substring的和是K的倍数。

暴力做法是遍历array的所有的substring，因为一个array有 `O(n^2)` 个substring， 所以复杂度是 `O(n^2)` 。

因为刚刚做了974，对里面用到的积分的做法印象很深刻。这一题做法和974完全一致，也是用积分和计数器做。

1.  给array做积分

    做完积分之后，把积分相信成一个柱状图，后面的柱子的高度减去前面的柱子的高度就是这一段substring的和。
    
    所以问题等效成，遍历每一根柱子，找到这根柱子后面比它的高k个单位的柱子的个数。这个个数就是所有从这根柱子开始到后面一根柱子结束这一段substring的和等于k的substring的个数 [#]_ 。

2.  遍历每个积分项，找到它后面比它正好大k个单位的其他积分项的个数

    可惜这样做，复杂度仍然是 `O(n^2)` ，因为遍历每个积分项的时候都需要从这个积分项往后遍历一遍，所以需要想一想怎样优化。
    
    因为是要数个数，所以很容易就想到用 `Counter` ，这样在遍历每个积分项的时候不需要遍历后面的项，瞬间就能知道后面有多少个比自己大k的项。

    那怎样才能做到从 **当前积分项往后面找** 、忽略前面的项呢？也很简单，每次找之前，先排除掉当前积分项，也就是把 `Counter` 里当前积分项出现的个数减一，这样每次查之前都排除掉当前积分项，就自动忽略了前面的项了。

.. [#] 我发现这个话用英文讲容易理解啊：This number is the number of all substrings that begins from this pillar to the pillar afterwards, that sums to k.
"""

from typing import *

import collections
import itertools

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        integral = [0] + list(itertools.accumulate(nums)) # 做积分
        counter = collections.Counter(integral) # 数每个积分项出现的次数
        res = 0

        for v in integral: # 遍历积分项
            counter[v] -= 1 # 排除当前积分项
            res += counter[v + k] # 查后面后多少项正好是当前项加上k

        return res

# s = Solution()
# print(s.subarraySum([1, 1, 1], 2)) # 2
# print(s.subarraySum([1, 1, 1, 1, 1], 2)) # 4