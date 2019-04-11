r"""
array里的每个元素代表如果你在那个位置，最多能往前跳的单位个数，问你能否跳到array的最后一格。

假设array是 :math:`a_0, a_1, a_2, ... a_{n - 1}` ，第i格是否可达用 :math:`p_i` 表示，那么能跳到 :math:`a_{n - 1}`的条件是

-   第n-2格的跳跃数大于等于1，并且第n-2格可达
-   或者 第n-3格的跳跃数大于等于2，并且第n-3格可达
-   或者 第n-4格的跳跃数大于等于3，并且第n-4格可达
-   ...
-   或者 第n-i格的跳跃数大于等于i-1，并且第n-i格可达
-   ...
-   或者 第1格的跳跃数大于等于n-2，并且第1个可达
-   或者 第0格的跳跃数大于等于n-1

即

.. math::

    \begin{aligned}
        & (a_{n - 2} \geq 1 \& p_{n - 2}) \\
        & (a_{n - 3} \geq 2 \& p_{n - 1}) \\
        & ... \\
        & (a_{n - i} \geq i - 1 \& p_{n - i}) \\
        & ... \\
        & (a_1 \geq n - 2 \& p_1) \\
        & (a_0 \geq n - 1)
    \end{aligned}
"""

from typing import *

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return True
        elif len(nums) == 1:
            return True
        else:
            dp = [True] # 起始就在第0格上，所以第0格可达

            for i, v in enumerate(nums[1: ], 1): # 看第i格是否可达

                for j in reversed(range(0, i)): # 从后往前扫描，看第i格可不可达
                    if nums[j] >= i - j and dp[j] == True: # 如果第j格可达、且能跳到i格
                        dp.append(True) # 说明第i格可达
                        break
                else: # 找了一圈都没找到从哪一格起跳能到达第i格，说明第i格不可达
                    dp.append(False)
            
            return dp[-1] # 最后一个是否可达

# s = Solution()
# assert s.canJump([2, 3, 1, 1, 4]) == True
# assert s.canJump([3, 2, 1, 0, 4]) == False