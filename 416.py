r"""
.. default-role:: math

给一个全是正整数的集合，问这个集合是否存在一个子集，它的和正好是整个集合的和的一半。

所谓“和正好是整个集合的一半”没有什么特殊的，换成“和正好是 `t` ”也是一样的，都是所谓的subset sum问题。

subset sum可以归约到背包问题。但是这里全是正整数，所以可以归约到整数背包问题，用DP来解，复杂度是伪多项式阶 `O(n t)` 。为什么是伪多项式阶呢，因为这里有个 `t` ，是输入的值、不是输入的 **规模** 。

一开始是用递归暴力的，超时了。后来想到不如DP的那种思路，把前 `i` 个元素所有能凑成的和都记下来，来了第 `i + 1` 个元素之后，只要把这个第 `i + 1` 个数加到前面所有的和上，就得到了前 `i + 1` 个元素所有能凑成的和。

假设 ``dp[i]`` 是前 `i` 个元素组成的集合的所有子集的和，那么 ``dp[i + 1]`` 和 ``dp[i]`` 的关系就是

.. math::

    \text{OPT}(i + 1) = \text{OPT}(i) \cup \{a_i\} \cup \{a_i + v | v \in \text{OPT}(i)\}

这里有两个地方可以优化

-   因为 ``dp[i]`` 只和前一项 ``dp[i - 1]`` 有关，所以不需要保存所有的 ``dp[i]`` ，永远只要保存前一项就可以了
-   因为集合里全都是正整数，所以越往后越加、和总是越来越大，那么大于 `t` 的和实际上是没有必要放在集合里的，反正都超过 `t` 了，再往后加也只会越来越大。也就是说递推式可以退化成

    .. math::

        \text{OPT}(i + 1) = \text{OPT}(i) \cup \{a_i\} \cup \{a_i + v | v \in \text{OPT}(i), a_i + v \leq t\}

    只有那些小于 `t` 的和才有希望加上 `a_i` 之后正好等于 `t` 。

这样做的话，复杂度和整数背包问题的DP做法是一模一样的，都是 `O(n t)` 。
"""

from typing import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2 # subset sum的目标和t
        summations = set() # dp[i - 1]，加到前一项之后，所有可能的和

        for v in nums:
            newSummations = {v}

            for summation in summations:
                if v + summation <= target: # 比target还大的就没必要放进去了，这样可以保证summations里面的元素个数一定小于target，复杂度也就锁定在伪多项式阶之下了
                    newSummations.add(v + summation)

            summations.update(newSummations)
            if target in summations:
                return True

        return False
