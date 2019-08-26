"""
.. default-role:: math

给员工分配任务，怎样分配才能获得最大收益？

``difficulty[i]`` 表示第 `i` 个任务的难度， ``profit[i]`` 表示第 `i` 个任务的汇报。 ``worker[i]`` 表示第 `i` 个员工的能力（也就是能完成的任务的最大难度），一个员工不能做超过自己能力的任务。每个员工只能做一个任务，但是每个任务可以被分配给多个员工。

注意一个坑：我们会想当然认为难度越高的任务，回报也越大，但是其实不是这样的。高难度的任务不一定回报比低难度的任务大。

所以第一件事情是要把每个难度 `d_i` 对应的回报 `p_i` ，转换成每个难度对应的 **最大回报** `p'_i` ，也就是说变成对于每个难度，找到小于等于这个难度的其他任务的最大回报

.. math::

    p'_i = \max\{p_j | d_j \leq d_i\}

如果有 `n` 个任务，暴力更新 `\{p'_i}` 的复杂度是 `O(n^2)` ，不过可以先给 `n` 个任务按难度从小到大排个序，这样复杂度降低到 `O(n \ln n)` 。

然后遍历每个员工，用二分搜索，找到小于等于这个员工能力的 **最难** 的任务 `d_i` ，这个员工能创造的最大回报就是 `p'_i` 了。

这样复杂度是 `O(n \ln n)` 。听说还有 `O(n)` 的做法，下次再想。

.. 突然想到996福报。
"""

from typing import *

import bisect

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficultyProfitMapping = {} # 可能会有两个任务难度相同但回报不同的情况，如果任务难度一样可是一个回报大一个回报小，谁会去做回报小的那个任务呢？所以先做一次过滤，只取回报大的那个任务的回报

        for i in range(len(difficulty)):
            if difficulty[i] in difficultyProfitMapping:
                difficultyProfitMapping[difficulty[i]] = max(difficultyProfitMapping[difficulty[i]], profit[i])
            else:
                difficultyProfitMapping[difficulty[i]] = profit[i]

        difficulties = sorted(difficultyProfitMapping.keys()) # 按难度排序
        maximumProfit = 0

        for difficulty in difficulties: # 把 难度：回报 变成 难度：最大回报
            maximumProfit = max(maximumProfit, difficultyProfitMapping[difficulty])
            difficultyProfitMapping[difficulty] = maximumProfit

        res = 0

        for v in worker: # 遍历每个员工，给每个员工分配员工能力范围内回报最大的任务
            maximumDifficultyForThisWorkerIndex = bisect.bisect_left(difficulties, v) # 可能取值是0, 1, 2, ..., len(difficulties)
            if maximumDifficultyForThisWorkerIndex == len(difficulties): # 这个员工能胜任任何工作
                profitForThisWorker = difficultyProfitMapping[difficulties[-1]] # 给他最难的工作
            elif difficulties[maximumDifficultyForThisWorkerIndex] == v: # 这个员工的能力恰好能胜任某份工作
                profitForThisWorker = difficultyProfitMapping[v]
            elif maximumDifficultyForThisWorkerIndex == 0: # 这个员工的能力没法胜任任何工作
                profitForThisWorker = 0 # profit是0
            else: # 这个员工能恰好能胜任难度低一级的工作
                maximumDifficultyForThisWorker = difficulties[maximumDifficultyForThisWorkerIndex - 1]
                profitForThisWorker = difficultyProfitMapping[maximumDifficultyForThisWorker]
            res = res + profitForThisWorker

        return res

# s = Solution()
# print(s.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])) # 100
# print(s.maxProfitAssignment([13,37,58], [4,90,96], [34,73,45])) # 190
# print(s.maxProfitAssignment([68,35,52,47,86], [67,17,1,81,3], [92,10,85,84,82])) # 324