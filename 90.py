"""
array的所有带重复的subset。

讲道理，这道题的意思我是真的不能理解。应该是不允许组合重复、但允许项重复。

最后还是屈服于 ``itertools.combinations()`` 了……
"""

from typing import *

import itertools

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # routes = self.getAllRoutesFromRoot(nums) + [[]]
        # print(routes)
        # res = list(map(list, set(map(tuple, map(sorted, routes)))))
        # print(res)
        # return res
        nums = sorted(nums)
        res = []

        for i in range(len(nums) + 1):
            res += list(map(list, set(itertools.combinations(nums, i))))
        
        return res

        
    # def getAllRoutesFromRoot(self, nums: List[int]) -> List[List[int]]: # 生成根节点到所有节点的路径
    #     if len(nums) == 1:
    #         return [nums]
    #     elif len(nums) > 1:
    #         res = []

    #         for i, v in enumerate(nums):
    #             res += [[v]]
    #             res += [[v] + route for route in self.getAllRoutesFromRoot(nums[: i] + nums[i + 1: ])]

    #         return res
    #     else:
    #         return []

# s = Solution()
# print(s.subsetsWithDup([4,4,4,1,4]))
# print(s.subsetsWithDup([1, 2, 3]))
# print(s.subsetsWithDup([1, 1]))
# print(s.subsetsWithDup([1, 2, 2]))
# print(s.subsetsWithDup([1,2,3,4,5,6,7,8,10,0]))