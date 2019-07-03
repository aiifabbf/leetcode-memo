"""
和39差不多，不过这里每个数字只能用一次，而39里可以用无限多次。

基本上可以完全套用39的代码，只要修改一下传给下一层的可用数列表就可以了，如果当前层用了这个数字，传给下一层的时候就不要再传这个数字就可以了。
"""

from typing import *

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = self.allRoutesToSum(candidates, target)
        return list(map(list, res))
        
    def allRoutesToSum(self, candidates: List[int], target: int) -> "Set[Tuple[int, ...]]":
        routes = set() # 用set保证路径不重复

        for i, candidate in enumerate(candidates):
            if candidate < target: # 加了这个数之后还是没法到target，那就再往下走试试看
                # newCandidates = candidates.copy()
                # newCandidates.remove(candidate) # 这个会有点慢是不是
                newCandidates = candidates[: i] + candidates[i + 1: ] # 这样会快一点吧
                routes.update((tuple(sorted(v + (candidate, ))) for v in self.allRoutesToSum(newCandidates, target - candidate)))
            elif candidate == target: # 加了这个数之后正好能得到target，不用再往下走了
                routes.add((candidate, )) # 同样题目里说了都是正数，所以到这里就不用再找下去了
            else: # 加了这个数之后超过target了，说明这条路径走不通
                pass
        
        return routes

# s = Solution()
# print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
# # [
# #   [1, 7],
# #   [1, 2, 5],
# #   [2, 6],
# #   [1, 1, 6]
# # ]
# print(s.combinationSum2([2, 5, 2, 1, 2], 5))
# # [
# #   [1,2,2],
# #   [5]
# # ]