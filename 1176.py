"""
取出一个array的所有长度是k的substring，求出这些substring的累加和。如果一个substring的累加和大于 ``upper`` ，加一分；如果一个substring的累加和小于 ``lower`` ，减一份；其他情况不加不减分。问最后分数是多少。

很啰嗦……还是直接求积分，这样每个substring的累加和就是 ``integral[i + k] - integral[i]`` 。然后用 ``integral[i + k] - integral[i]`` 的老套路了。
"""

from typing import *

import itertools

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        integral = [0] + list(itertools.accumulate(calories)) # 求积分
        res = 0 # 记录最终的分数

        for i in range(len(integral) - k): # 长度为k的substring总共有n - k个
            caloriesDuringThisPeriod = integral[i + k] - integral[i] # calories[i: i + k]的累加和
            if caloriesDuringThisPeriod > upper: # substring的累加和大于upper
                res += 1 # 加一分
            elif caloriesDuringThisPeriod < lower: # substring的累加和小于lower
                res -= 1 # 减一分
            else: # 其他情况
                pass # 不加分也不减分
        
        return res

# s = Solution()
# print(s.dietPlanPerformance([1, 2, 3, 4, 5], 1, 3, 3)) # 0
# print(s.dietPlanPerformance([3, 2], 2, 0, 1)) # 1