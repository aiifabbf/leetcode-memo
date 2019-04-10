r"""
求一个array的所有substring最小值的和

就是求

.. math::

    \sum_{0 \leq i < j \leq n} \min\{a_i, a_{i + 1}, ... a_j\}

第一反应是动态规划，因为这种substring的题最喜欢动态规划，然后我也确实发现了这里有可以缓存的东西。

设 :math:`\{p_i\}` 是以第i个元素结尾的所有的substring的最小值，如果 :math:`a_i` 比前面一个元素大或者相等，那么 :math:`\{p_i\} = \{\{p_{i - 1}\}, a_i\}` ；如果 :math:`a_i` 比前面的元素小，那么就要再往前看一格，直到看到前面有一个元素比当前元素小或者相等的。

可惜这个方法内存复杂度 :math:`O(n^2)` ……因为要存一张右上三角形状的巨大的dp表。

然后突然发现其实根本没必要存整个 :math:`\{p_i\}` ，直接存 :math:`\sum\{p_i\}` 就可以了，反正只会用到和，这样内存复杂度就降到 :math:`O(n)` 了。

但是时间复杂度又出问题了，最好情况是array递增，这时候每次往前看一格就可以退出内循环，所以时间复杂度是 :math:`O(n)` ，但是如果array递减，每次往前看都要看到array的最开头，所以时间复杂度马上劣化到 :math:`O(n^2)` 。

所以这里加速的关键是如何从后往前，快速找到离当前元素最近的、比当前元素小或相等的元素的下标。假设用 :math:`\{x_i\}` 表示array前面，离第i个元素最近的、比第i个元素小或相等的元素的下标。最naive的方法就是每次到一个元素，都从这个元素从后往前一个一个比较，那么如果array刚好是递减的，复杂度就是 :math:`O(n^2)` ，所以没有省时间；有 :math:`O(n)` 的方法是用单调递增stack来做。


"""

from typing import *

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # dp = [
        #     [A[0]]
        # ]
        stack = [] # 单调递增stack，里面存的是 (i, v) 其中v是从底到顶单调递增的
        nearestLessOrEqualElementPosition = [-1] * len(A) # 初始化数组，nearestLessOrEqualElementPosition[i] 表示的是，第i个元素前面最近的、比第i个元素小或者相等的元素的下标。

        for i, v in enumerate(A):
            
            while stack != [] and stack[-1][1] > v: # stack顶上的元素比当前元素大
                stack.pop() # 所以要pop掉
            # 出while循环之后，stack要么是空的，要么顶部的那个元素小于等于v，也就定位到了第i个元素前面最近的、比第i个元素小或相等的元素和下标

            if stack == []: # 如果stack空了，说明第i个元素前面不存在比自己小或者相等的元素，即第i个元素前面的元素全都比自己大
                nearestLessOrEqualElementPosition[i] = -1 # 用-1表示没有
            else: # stack没空，说明前面确实存在小于等于第i个元素的元素，并且最近的元素就刚好在stack顶部
                nearestLessOrEqualElementPosition[i] = stack[-1][0] # 所以找到了，记录一下
            stack.append((i, v)) # 再把当前元素放进stack
        # print(nearestLessOrEqualElementPosition)
        dp = [
            A[0],
        ] # 反正只会用到和，所以就只存和就好了
        maximumPosition = 0
        summation = A[0]

        for i, v in enumerate(A[1: ], 1):
            # minimumOfSubarraysEndingHere = [v] # 单元素也是一个substring
            minimumSummationOfSubarraysEndingHere = v

            # for j in reversed(range(0, i)): # 从后往前看，快速找到离当前元素最近的、小于或等于当前元素的元素
                # if A[j] <= v: # 当前元素比前面的某个元素大或者相等
                #     # minimumOfSubarraysEndingHere.append(dp[j]) # 直接把前面的这个元素的dp抄过来
                #     minimumSummationOfSubarraysEndingHere += dp[j]
                #     break
                # else: # 当前元素比前面的某个元素小
                #     # minimumOfSubarraysEndingHere.append(v) # 再往前看看
                #     minimumSummationOfSubarraysEndingHere += v
            # 有了nearestLessOrEqualElementPosition之后，马上就知道第i个元素前面最近的比它小的元素的下标了
            if nearestLessOrEqualElementPosition[i] == -1:
                minimumSummationOfSubarraysEndingHere += v * i
            else:
                minimumSummationOfSubarraysEndingHere += dp[nearestLessOrEqualElementPosition[i]] + v * (i - nearestLessOrEqualElementPosition[i] - 1)

            # summation += sum(minimumOfSubarraysEndingHere)
            # summation += self.sumFlattenList(minimumOfSubarraysEndingHere)
            summation += minimumSummationOfSubarraysEndingHere

            # dp.append(minimumOfSubarraysEndingHere)
            dp.append(minimumSummationOfSubarraysEndingHere)

        return summation % (10**9 + 7)

# s = Solution()
# print(s.sumSubarrayMins([3, 1, 2, 4]))