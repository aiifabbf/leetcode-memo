"""
从1到9里挑k个数字，使得它们的和是n，输出所有可能的组合。不允许重复项、不允许重复组合。

和39题类似，只是这里不允许重复项也不允许重复组合。那我寻思着n不是最大只能 :math:`1 + 2 + ... + 9 = 45` ？

而且组合数也并不是很多，1到9不重复选k个数字，总共有 :math:`C_9^k` 种组合，其中 :math:`k = 4, 5` 的时候，组合数最多，但是也就是 :math:`C_9^4 = C_9^5 = 126` 种，所以这道题直接暴力搜索是完全可以的。
"""

from typing import *

import itertools

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return list(list(v) for v in itertools.combinations(range(1, 10), k) if sum(v) == n) # 暴力搜索