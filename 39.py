"""
给一个array，得到所有加和是target的组合，允许某一个数字用无限次。

观察发现每一步的选择受到一些限制，同时在做选择的时候能提前知道做出了这个选择之后，下面的选择是否有意义，果断意识到这是一道决策树的题目 [#]_ ，那就按照决策树的套路来做吧，题目的目标转换成找到决策树里所有路径和为target的路径、再经过一次过滤（因为不允许重复组合）。

.. [#] 22是我做过的第一道决策树的题目。

题目说允许一个数字用无限次，所以每一步都可以选择 ``candidates`` 中的任意一个元素。

遍历过程中受到的唯一的限制是，路径和不能超过目标和。如果发现加到某个节点，路径和超过目标和了，以这个节点为根节点的子树整个都可以忽略掉了，因为题目说了节点值全部是正数，继续加下去只会使路径和越来越大，所以没有必要再遍历下去了。同样，如果发现加到某个节点，路径和刚好等于目标和，也没有必要继续下去了。

得到所有符合条件的路径之后还不能马上return，因为遍历的时候没有考虑节点值重复，所以必定会出现重复组合，简单过滤一下结果就可以return了。

我用的过滤的方法是，先把每条路径都从小到大排序，然后变成tuple [#]_ ，再放到set里面，再转换回list，就可以了。

.. [#] 因为set要求里面的元素都是hashable的。类似list的对象是unhashable的。注意这个hashable和mutable没有必然联系，一个mutable对象可以是hashable的。
"""

from typing import *

# import collections

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        routes = self.findAllRoutesSumToTarget(candidates, target)
        # print(list(map(list, set(map(tuple, map(sorted, routes))))))
        return list(set(map(tuple, map(sorted, routes)))) # 简单过滤一下就可以return了。这里过滤用的方法是

    def findAllRoutesSumToTarget(self, candidates: List[int], target: int) -> List[List[int]]: # 不考虑重复路径
        res = []
        
        for v in candidates:
            if v < target: # 加到这里为止，路径和还没有到target，那么有必要继续往下找
                res += [[v] + route for route in self.findAllRoutesSumToTarget(candidates, target - v)] # 往下找有没有和为target - v的路径
            elif v == target:
                res += [
                    [v]
                ]
                # res += [[v] + route for route in self.findAllRoutesSumToTarget(candidates, target - v)] # 因为题目有条件，array里所有的数字都是正数，所以遇到路径和到这里正好加完的，不用再往下找了，到这里为止就可以了。即便往下找，只会让路径和越来越大。
            else: # v > target。不用考虑往下遍历了，因为没有负数，往下找路径和只会越来越大，所以直接整个子树跳过，直接不用找了。
                pass

        return res

# s = Solution()
# assert s.combinationSum([2, 3, 6, 7], 7) == [
#     [7],
#     [2, 2, 3]
# ]
# assert s.combinationSum([2, 3, 5], 8) == [
#     [2, 2, 2, 2],
#     [2, 3, 3],
#     [3, 5]
# ]