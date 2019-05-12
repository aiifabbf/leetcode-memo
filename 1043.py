"""
把array切成许多长度不超过K的substring（要连续），然后把每个substring里的元素都设置成这个substring里的最大值，问这之后所有substring的和最大是多少。

居然还是DP。

用 ``dp[i]`` 表示以第i个元素结尾的array的最大分片和，思考 ``dp[i]`` 和前面的项的关系。因为最大分片长度是K，所以第i个元素可以有这几种情况

-   单独成片，即第i个元素单独成一个长度为1的substring

    这时分片和是 ``dp[i - 1] + A[i]``

-   和第i-1个元素成片，即第i-1个元素和第i个元素成一个长度为2的substring

    这时分片和是 ``dp[i - 2] + max(A[i - 1], A[i]) * 2``

-   和第i-1个、第i-2个元素成片，即第i-2个元素、第i-1个元素和第i个元素成一个长度为3的substring

    这时分片和是 ``dp[i - 3] + max(A[i - 2], A[i - 1], A[i]) * 3``

-   ...
-   和第i-j个元素及之后的所有元素成片，组成一个长度为j+1的substring

    这时分片和是 ``dp[i - j - 1] + max(A[i - j], A[i - j + 1], ... A[i]) * (j + 1)``

-   ...
-   和第i-(K-1)个元素之后的所有元素成片，组成一个长度为K的substring

    这时分片和是 ``dp[i - (K - 1) - 1] + max(A[i - (K - 1)], A[i - (K - 1) + 1], ..., A[i]) * K``

``dp[i]`` 就是上面这K种情况里，分片和的最大值。

简单来说，就是试着用第i个元素和前面的元素组成长度为1、2、...、K的substring，看哪个分片和最大。

此外要注意第i个元素前面可能没有K个那么多元素。
"""

from typing import *

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if K == 1:
            return sum(A)
        else:
            dp = [A[0]] # 初始条件，第0个元素当然只能单独成片

            for i, v in enumerate(A[1: ], 1): # 从第1个元素开始遍历
                maximumSummationEndingHere = v + dp[-1] # 第i个元素单独成片的分片总和
                maxNumberInThisSection = v # 当前片的最大值。虽然不会改变复杂度阶数，但是会变快

                for sectionLength in range(2, K + 1): # 第i个元素和前面的元素形成长度为2, 3, ..., K的substring
                    sectionSeparatorPosition = i - (sectionLength - 1) # 分界点的位置
                    if sectionSeparatorPosition < 0: # 如果分界点小于0了
                        break # 后面的不用看了，说明前面没有足够多的元素
                    elif sectionSeparatorPosition == 0: # 分界点正好在0上
                        maxNumberInThisSection = max(A[sectionSeparatorPosition], maxNumberInThisSection) # 更新当前片的最大值
                        maximumSummationEndingHere = max(maxNumberInThisSection * sectionLength, maximumSummationEndingHere) # 因为分界点正好在0上，所以没有dp[-1]
                        # 我写到这里感觉怪怪的，应该遵循[)原则，用dp[i]表示以第i-1个为结尾的array的最大分片和，不过写都写了。
                    else: # 分界点大于0
                        maxNumberInThisSection = max(A[sectionSeparatorPosition], maxNumberInThisSection) # 更新当前片的最大值
                        maximumSummationEndingHere = max(dp[sectionSeparatorPosition - 1] + maxNumberInThisSection * sectionLength, maximumSummationEndingHere) # 跟踪最大分片和

                dp.append(maximumSummationEndingHere)

        # print(dp)

        return dp[-1] # 结果直接是dp的最后一个元素

# s = Solution()
# print(s.maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)) # 84
# print(s.maxSumAfterPartitioning([8, 5, 7], 3)) # 24